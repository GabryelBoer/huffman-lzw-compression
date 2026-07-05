# Resultados do Benchmark: Huffman vs LZW

## Objetivo

Comparar Huffman e LZW na compressao lossless de codigo-fonte, medindo taxa de compressao, tempo de execucao, uso de memoria e correlacao com perfil de redundancia lexical e entropia de Shannon.

## Dataset

| Arquivo | Categoria | Tamanho | Entropia | Repeticao lexical |
|---------|-----------|---------|----------|-------------------|
| encoder_sample.py | py_pequeno | 1 059 B | 4.69 | 0.12 |
| lzw_encoder_sample.py | py_pequeno | 2 233 B | 4.77 | 0.11 |
| high_entropy_payload.py | py_medio | 13 793 B | 6.02 | 0.00 |
| requests_sessions.py | py_medio | 34 072 B | 4.50 | 0.13 |
| jansson_dump.c | c_medio | 14 326 B | 4.31 | 0.20 |
| access.log | baseline_log | 17 599 B | 4.13 | 0.00 |

## Resultados por Arquivo

### Codigo-fonte Python

**requests_sessions.py (34 KB)**
- Huffman: taxa 1.73, economia 42.1%, compressao 37 ms, memoria 110 KB
- LZW: taxa 1.66, economia 39.7%, compressao 35 ms, descompressao 14 ms, memoria 871 KB
- Huffman vence em taxa; LZW vence em tempo de descompressao

**encoder_sample.py (1 KB)**
- Huffman: taxa 1.19, economia 15.9%
- LZW: taxa 0.98 (expansao), economia -1.6%
- Arquivo pequeno: overhead do dicionario LZW supera ganho

**high_entropy_payload.py (14 KB)**
- Huffman: taxa 1.28, economia 22.1%
- LZW: taxa 0.75 (expansao), economia -33.6%
- Alta entropia: Huffman superior; LZW expande o arquivo

### Codigo-fonte C

**jansson_dump.c (14 KB)**
- Huffman: taxa 1.73, economia 42.0%
- LZW: taxa 1.90, economia 47.4%
- LZW vence em taxa; Huffman usa menos memoria (66 vs 568 KB)

### Baseline (log repetitivo)

**access.log (18 KB)**
- Huffman: taxa 1.89, economia 47.0%
- LZW: taxa 6.76, economia 85.2%
- Fora do dominio de codigo-fonte, LZW domina por padroes longos repetidos

## Analise Teorica vs Pratica

| Criterio | Huffman | LZW | Observacao experimental |
|----------|---------|-----|-------------------------|
| Complexidade tempo | O(n log n) + O(m) | O(m) amortizado | Tempos similares em arquivos medios |
| Complexidade espaco | Arvore + tabela no arquivo | Dicionario em memoria | Huffman usa 5-10x menos memoria |
| Metadados extras | Sim (frequencias) | Nao | Confirmado no formato .huf vs .lzw |
| Cenario ideal | Frequencias desiguais | Padroes repetidos | Confirmado em log e .c |
| Facilidade | Moderada (heap+arvore) | Moderada (dict+edge cases) | Empate tecnico |

## Correlacao Perfil x Desempenho (contribuicao inedita)

1. **Alta repeticao lexical + entropia moderada** (jansson_dump.c, requests_sessions.py): ambos competitivos; LZW levemente melhor em .c, Huffman em .py grande
2. **Arquivos pequenos** (< 2 KB): Huffman evita expansao; LZW pode aumentar tamanho
3. **Alta entropia** (payload com dados embutidos): Huffman comprime; LZW expande
4. **Logs repetitivos** (baseline): LZW muito superior (taxa 6.76 vs 1.89)

Formula de decisao pratica:
- Codigo-fonte tipico de repositorio: Huffman para arquivos pequenos e alta entropia; LZW para arquivos C com tokens repetidos; empate em arquivos Python medios
- Prioridade memoria: Huffman
- Prioridade velocidade de descompressao: LZW

## Conclusoes Parciais

1. Nao ha vencedor absoluto em codigo-fonte; o melhor algoritmo depende do perfil do arquivo
2. Huffman e mais previsivel e usa menos memoria
3. LZW pode expandir arquivos pequenos ou de alta entropia
4. Em padroes altamente repetitivos (logs), LZW supera Huffman significativamente
5. Todos os testes validaram integridade lossless (SHA-256)

## Graficos

- `benchmark-plots/compression-ratio.png`
- `benchmark-plots/tempo-execucao.png`
- `benchmark-plots/memoria.png`

## Como Reproduzir

```bash
bash run-all.sh
```

Arquivo agregado: `results/compression-summary.csv`
