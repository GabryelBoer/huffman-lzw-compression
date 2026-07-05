# Resultados do Benchmark: Huffman vs LZW

## Objetivo

Comparar Huffman e LZW na compressao lossless de codigo-fonte, medindo taxa de compressao, tempo de execucao, uso de memoria e correlacao com perfil de redundancia lexical e entropia de Shannon.

Dados gerados localmente via `bash run-all.sh`. Todos os testes validaram integridade lossless (SHA-256).

## Dataset

| Arquivo | Categoria | Tamanho | Entropia | Repeticao lexical |
|---------|-----------|---------|----------|-------------------|
| encoder_sample.py | py_pequeno | 1 059 B | 4.69 | 0.12 |
| lzw_encoder_sample.py | py_pequeno | 2 233 B | 4.77 | 0.11 |
| high_entropy_payload.py | py_medio | 13 793 B | 6.02 | 0.00 |
| requests_sessions.py | py_medio | 34 072 B | 4.50 | 0.13 |
| jansson_dump.c | c_medio | 14 326 B | 4.31 | 0.20 |
| access.log | baseline_log | 17 599 B | 4.13 | 0.00 |

## Tabela Consolidada

| Arquivo | Algoritmo | Taxa | Economia (%) | Comp. (ms) | Descomp. (ms) | Mem. (KB) |
|---------|-----------|------|--------------|------------|---------------|-----------|
| requests_sessions.py | Huffman | 1.73 | 42.10 | 35.5 | 34.1 | 110.4 |
| requests_sessions.py | LZW | 1.66 | 39.73 | 33.0 | 13.4 | 870.7 |
| jansson_dump.c | Huffman | 1.73 | 42.04 | 15.1 | 13.5 | 66.3 |
| jansson_dump.c | LZW | 1.90 | 47.35 | 14.2 | 9.0 | 567.9 |
| encoder_sample.py | Huffman | 1.19 | 15.86 | 1.4 | 1.3 | 20.5 |
| encoder_sample.py | LZW | 0.98 | -1.61 | 1.4 | 1.3 | 98.6 |
| lzw_encoder_sample.py | Huffman | 1.33 | 24.63 | 2.9 | 2.6 | 27.5 |
| lzw_encoder_sample.py | LZW | 1.18 | 15.09 | 2.7 | 2.3 | 132.6 |
| high_entropy_payload.py | Huffman | 1.28 | 22.07 | 17.9 | 18.5 | 64.0 |
| high_entropy_payload.py | LZW | 0.75 | -33.60 | 17.6 | 11.5 | 695.4 |
| access.log | Huffman | 1.89 | 46.98 | 19.3 | 16.4 | 50.1 |
| access.log | LZW | 6.76 | 85.22 | 14.5 | 3.2 | 263.6 |

## Graficos

### Figura 1: Taxa de compressao por arquivo

![Taxa de compressao](benchmark-plots/compression-ratio.png)

**Leitura:** barras mais altas indicam melhor compressao. LZW destaca-se no baseline `access.log` (taxa 6.76) e em `jansson_dump.c` (1.90). Huffman mantem vantagem em `requests_sessions.py`, arquivos pequenos e `high_entropy_payload.py`.

### Figura 2: Tempo de compressao

![Tempo de compressao](benchmark-plots/tempo-execucao.png)

**Leitura:** tempos de compressao sao proximos entre Huffman e LZW na maioria dos arquivos. A maior diferenca pratica aparece na descompressao (ver CSV), onde LZW e mais rapido em arquivos medios.

### Figura 3: Uso de memoria

![Uso de memoria](benchmark-plots/memoria.png)

**Leitura:** Huffman usa de 5x a 10x menos memoria que LZW. O dicionario adaptativo do LZW cresce com o tamanho do arquivo, chegando a 870 KB em `requests_sessions.py`.

## Resultados por Arquivo

### Codigo-fonte Python

**requests_sessions.py (34 KB)**
- Huffman: taxa 1.73, economia 42.1%, memoria 110 KB
- LZW: taxa 1.66, economia 39.7%, descompressao 13.4 ms (2.5x mais rapida), memoria 871 KB
- Huffman vence em taxa e memoria; LZW vence em descompressao

**encoder_sample.py (1 KB)**
- Huffman: taxa 1.19, economia 15.9%
- LZW: taxa 0.98 (expansao), economia -1.6%
- Arquivo pequeno: overhead do dicionario LZW supera ganho

**high_entropy_payload.py (14 KB)**
- Huffman: taxa 1.28, economia 22.1%
- LZW: taxa 0.75 (expansao), economia -33.6%
- Alta entropia (6.02 bits): Huffman superior; LZW expande o arquivo

### Codigo-fonte C

**jansson_dump.c (14 KB)**
- Huffman: taxa 1.73, economia 42.0%, memoria 66 KB
- LZW: taxa 1.90, economia 47.4%, descompressao 9.0 ms, memoria 568 KB
- LZW vence em taxa e descompressao; Huffman vence em memoria

### Baseline (log repetitivo)

**access.log (18 KB)**
- Huffman: taxa 1.89, economia 47.0%
- LZW: taxa 6.76, economia 85.2%, descompressao 3.2 ms
- Fora do dominio de codigo-fonte, LZW domina por padroes longos repetidos

## Analise Teorica vs Pratica

| Criterio | Huffman | LZW | Observacao experimental |
|----------|---------|-----|-------------------------|
| Complexidade tempo | O(n log n) + O(m) | O(m) amortizado | Tempos similares em compressao |
| Complexidade espaco | Arvore + tabela no arquivo | Dicionario em memoria | Huffman usa 5-10x menos memoria |
| Metadados extras | Sim (frequencias) | Nao | Confirmado nos formatos .huf e .lzw |
| Cenario ideal | Frequencias desiguais | Padroes repetidos | Confirmado em log e .c |
| Facilidade | Moderada (heap+arvore) | Moderada (dict+edge cases) | Empate tecnico |

## Correlacao Perfil x Desempenho

1. **Alta repeticao lexical + entropia moderada** (`jansson_dump.c`, taxa lexical 0.20): LZW vence em taxa (1.90 vs 1.73)
2. **Arquivos pequenos** (< 2 KB): Huffman evita expansao; LZW pode aumentar tamanho (`encoder_sample.py`)
3. **Alta entropia** (6.02 bits, repeticao lexical 0.00): Huffman comprime (1.28); LZW expande (0.75)
4. **Logs repetitivos** (baseline): LZW muito superior (taxa 6.76 vs 1.89)

**Regra pratica derivada dos dados:**
- Prioridade memoria: Huffman
- Prioridade taxa em codigo C repetitivo: LZW
- Prioridade taxa em alta entropia: Huffman
- Prioridade descompressao rapida: LZW

## Conclusoes

1. Nao ha vencedor absoluto em codigo-fonte
2. Huffman e mais previsivel e usa menos memoria
3. LZW pode expandir arquivos pequenos ou de alta entropia
4. Em padroes altamente repetitivos, LZW supera Huffman significativamente
5. Todos os 12 experimentos validaram integridade lossless

## Como Reproduzir

```bash
bash run-all.sh
```

Saida: `results/compression-summary.csv` e graficos em `benchmark-plots/`.
