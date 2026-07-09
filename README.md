# Compressao Huffman vs LZW em Codigo-Fonte

## Overview

Comparacao de Huffman e LZW na compressao lossless de arquivos de codigo-fonte (.py e .c) para armazenamento em repositorios. Trabalho AED-II - UFABC.

## Case Study

Compressao de codigo-fonte: reducao de tamanho para backup/versionamento sem perda de informacao. Huffman e LZW oferecem trade-offs entre taxa, velocidade e memoria.

## Algorithms

**Huffman:** arvore binaria adaptada a frequencia de simbolos. O(n log n) construccao, O(n) encoding/decoding. Memoria eficiente (20-110 KB).

**LZW:** dicionario dinamico com codigos variaveis. O(n) encoding/decoding. Padroes repetitivos. Memoria alta (98-870 KB, max 4096 entradas).

## Complexity Analysis

| Arquivo | Huffman Taxa | LZW Taxa | Huffman Tempo (ms) | LZW Tempo (ms) | Huffman Memoria (KB) | LZW Memoria (KB) |
|---------|---------|---------|---------|---------|---------|---------|
| requests_sessions.py | 1.73 | 1.66 | 35.5→34.1 | 33.0→13.4 | 110.4 | 870.7 |
| jansson_dump.c | 1.73 | 1.90 | 15.1→13.5 | 14.2→9.0 | 66.3 | 567.9 |
| access.log (baseline) | 1.89 | 6.76 | 19.3→16.4 | 14.5→3.2 | 50.1 | 263.6 |

Conclusao: Huffman vence em memoria; LZW em padroes repetitivos e descompressao rapida.

## Installation

**Pre-requisitos:** Python 3.11+, matplotlib, numpy, pytest

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Usage

```bash
bash run-all.sh
```

Executa benchmark em `data/` (codigo-fonte .py/.c + baseline .log) e gera:
- `results/compression-summary.csv` (resumo)
- `results/compression-detail-*.csv` (por arquivo)
- `benchmark-plots/*.png` (graficos)

## Results

**Dados:** coletados em Python 3.14, macOS (Jul 5).

![Taxa de compressao](benchmark-plots/compression-ratio.png)
![Tempo de execucao](benchmark-plots/tempo-execucao.png)
![Uso de memoria](benchmark-plots/memoria.png)

**Estrutura do Repositorio:**
```
src/huffman/           encode/decode, tree, heap
src/lzw/               encode/decode, dicionario hash
data/codigo/           arquivos .py e .c
tests/                 round-trip SHA-256
run-all.sh, plot-results.py
```

Huffman vence em entropia alta + memoria. LZW vence em padroes (C) + descompressao.

## Validation

Round-trip verification: SHA-256(original) == SHA-256(decompress(compress(original))) para todos os testes. Veja [CHECKLIST.md](CHECKLIST.md) e [RESULTADOS-BENCHMARK.md](RESULTADOS-BENCHMARK.md).
