# Compressao Huffman vs LZW em Codigo-Fonte

Comparacao de Huffman e LZW na compressao lossless de arquivos de codigo-fonte (.py e .c) para armazenamento e versionamento de repositorios de software.

Trabalho da disciplina **Algoritmos e Estruturas de Dados II (AED-II)** - UFABC.

## Resultados Principais

Dados coletados com `bash run-all.sh` em ambiente local (Python 3.14, macOS).

| Arquivo | Algoritmo | Taxa | Economia (%) | Compressao (ms) | Descompressao (ms) | Memoria (KB) |
|---------|-----------|------|--------------|-----------------|--------------------|--------------|
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
| access.log (baseline) | Huffman | 1.89 | 46.98 | 19.3 | 16.4 | 50.1 |
| access.log (baseline) | LZW | 6.76 | 85.22 | 14.5 | 3.2 | 263.6 |

## Visualizacoes

### Taxa de compressao por arquivo

![Taxa de compressao](benchmark-plots/compression-ratio.png)

Huffman vence em `requests_sessions.py` e arquivos de alta entropia. LZW vence em `jansson_dump.c` e no baseline `access.log`.

### Tempo de compressao

![Tempo de execucao](benchmark-plots/tempo-execucao.png)

Tempos de compressao ficam proximos entre os algoritmos. A diferenca maior aparece na descompressao de arquivos medios com LZW.

### Uso de memoria

![Uso de memoria](benchmark-plots/memoria.png)

Huffman usa consistentemente menos memoria (20 a 110 KB) que LZW (98 a 870 KB) por causa do dicionario adaptativo.

## Estrutura do Repositorio

```
src/
  huffman/          # heap, arvore, encode/decode
  lzw/              # dicionario hash, encode/decode
  io/               # bitstream
  benchmark/        # compare, metrics, profile
data/codigo/        # arquivos .py e .c de teste
data/baseline/      # log de contraste
results/            # CSVs do benchmark
benchmark-plots/    # graficos PNG
tests/              # testes round-trip
article/            # artigo em Word (artigo.docx)
slides/             # apresentacao PDF
run-all.sh          # executa benchmark completo
plot-results.py     # gera graficos
```

## Pre-requisitos

- Python 3.11+
- matplotlib, numpy, pytest

## Como Executar

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
bash run-all.sh
```

O script executa o benchmark em `data/` e gera:
- `results/compression-summary.csv`
- `results/compression-detail-*.csv`
- `benchmark-plots/compression-ratio.png`
- `benchmark-plots/tempo-execucao.png`
- `benchmark-plots/memoria.png`

## Parametros do Benchmark

| Parametro | Valor |
|-----------|-------|
| Algoritmos | Huffman, LZW |
| Tipos de arquivo | .py, .c, .log (baseline) |
| Metricas | taxa, fator, economia, tempo, memoria, entropia, repeticao lexical |
| Validacao | SHA-256 round-trip (lossless) |
| Dicionario LZW max | 4096 entradas |

## Documentacao

| Documento | Conteudo |
|-----------|----------|
| [RESULTADOS-BENCHMARK.md](RESULTADOS-BENCHMARK.md) | Analise detalhada com graficos e correlacao perfil-desempenho |
| [article/artigo.docx](article/artigo.docx) | Artigo cientifico completo (estrutura do guia do grupo) |
| [CHECKLIST.md](CHECKLIST.md) | Checklist de entrega AED-II |

## Conclusao Resumida

Nao ha vencedor absoluto em codigo-fonte. Huffman e mais efetivo em memoria, arquivos pequenos e alta entropia. LZW e mais efetivo em padroes repetitivos (codigo C e logs) e em velocidade de descompressao.
