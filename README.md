# Compressao Huffman vs LZW em Codigo-Fonte

Comparacao de Huffman e LZW na compressao lossless de arquivos de codigo-fonte (.py e .c) para armazenamento e versionamento de repositorios de software.

Trabalho da disciplina **Algoritmos e Estruturas de Dados II (AED-II)** - UFABC.

## Resultados Principais

| Arquivo | Algoritmo | Taxa | Economia (%) | Compressao (ms) | Descompressao (ms) | Memoria (KB) |
|---------|-----------|------|--------------|-----------------|--------------------|--------------|
| requests_sessions.py | Huffman | 1.73 | 42.10 | 37.1 | 36.5 | 110.4 |
| requests_sessions.py | LZW | 1.66 | 39.73 | 35.3 | 14.1 | 870.7 |
| jansson_dump.c | Huffman | 1.73 | 42.04 | 16.2 | 14.3 | 66.3 |
| jansson_dump.c | LZW | 1.90 | 47.35 | 15.3 | 9.8 | 567.9 |
| encoder_sample.py | Huffman | 1.19 | 15.86 | 1.5 | 1.3 | 20.5 |
| encoder_sample.py | LZW | 0.98 | -1.61 | 1.4 | 1.4 | 98.6 |
| high_entropy_payload.py | Huffman | 1.28 | 22.07 | 18.8 | 19.2 | 64.0 |
| high_entropy_payload.py | LZW | 0.75 | -33.60 | 18.4 | 12.4 | 695.4 |
| access.log (baseline) | Huffman | 1.89 | 46.98 | 18.7 | 16.5 | 50.1 |
| access.log (baseline) | LZW | 6.76 | 85.22 | 15.2 | 3.3 | 263.6 |

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
article/            # artigo cientifico (template SBC)
slides/             # apresentacao
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

O script executa o benchmark em `data/` e gera CSVs em `results/` e graficos em `benchmark-plots/`.

## Parametros do Benchmark

| Parametro | Valor |
|-----------|-------|
| Algoritmos | Huffman, LZW |
| Tipos de arquivo | .py, .c, .log (baseline) |
| Metricas | taxa, fator, economia, tempo, memoria, entropia, repeticao lexical |
| Validacao | SHA-256 round-trip (lossless) |
| Dicionario LZW max | 4096 entradas |

## Documentacao Detalhada

Veja [RESULTADOS-BENCHMARK.md](RESULTADOS-BENCHMARK.md) para analise completa, correlacao perfil x desempenho e conclusoes.

Repositorio: https://github.com/GabryelBoer/huffman-lzw-compression
