#!/usr/bin/env python3
import csv
from collections import defaultdict
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
PLOTS = ROOT / "benchmark-plots"


def load_summary() -> list[dict]:
    path = RESULTS / "compression-summary.csv"
    with path.open(encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def plot_compression_ratio(rows: list[dict]) -> None:
    files = sorted({row["arquivo"] for row in rows})
    x = np.arange(len(files))
    width = 0.35
    huffman = [float(next(r["taxa_compressao"] for r in rows if r["arquivo"] == f and r["algoritmo"] == "Huffman")) for f in files]
    lzw = [float(next(r["taxa_compressao"] for r in rows if r["arquivo"] == f and r["algoritmo"] == "LZW")) for f in files]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(x - width / 2, huffman, width, label="Huffman")
    ax.bar(x + width / 2, lzw, width, label="LZW")
    ax.set_ylabel("Taxa de compressao")
    ax.set_title("Taxa de compressao por arquivo")
    ax.set_xticks(x)
    ax.set_xticklabels(files, rotation=25, ha="right")
    ax.legend()
    fig.tight_layout()
    fig.savefig(PLOTS / "compression-ratio.png", dpi=150)
    plt.close(fig)


def plot_execution_time(rows: list[dict]) -> None:
    files = sorted({row["arquivo"] for row in rows})
    x = np.arange(len(files))
    width = 0.35
    huffman = [float(next(r["tempo_compressao_ms"] for r in rows if r["arquivo"] == f and r["algoritmo"] == "Huffman")) for f in files]
    lzw = [float(next(r["tempo_compressao_ms"] for r in rows if r["arquivo"] == f and r["algoritmo"] == "LZW")) for f in files]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(x - width / 2, huffman, width, label="Huffman")
    ax.bar(x + width / 2, lzw, width, label="LZW")
    ax.set_ylabel("Tempo de compressao (ms)")
    ax.set_title("Tempo de compressao por arquivo")
    ax.set_xticks(x)
    ax.set_xticklabels(files, rotation=25, ha="right")
    ax.legend()
    fig.tight_layout()
    fig.savefig(PLOTS / "tempo-execucao.png", dpi=150)
    plt.close(fig)


def plot_memory(rows: list[dict]) -> None:
    files = sorted({row["arquivo"] for row in rows})
    x = np.arange(len(files))
    width = 0.35
    huffman = [float(next(r["memoria_pico_kb"] for r in rows if r["arquivo"] == f and r["algoritmo"] == "Huffman")) for f in files]
    lzw = [float(next(r["memoria_pico_kb"] for r in rows if r["arquivo"] == f and r["algoritmo"] == "LZW")) for f in files]

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(x - width / 2, huffman, width, label="Huffman")
    ax.bar(x + width / 2, lzw, width, label="LZW")
    ax.set_ylabel("Memoria pico (KB)")
    ax.set_title("Uso de memoria por arquivo")
    ax.set_xticks(x)
    ax.set_xticklabels(files, rotation=25, ha="right")
    ax.legend()
    fig.tight_layout()
    fig.savefig(PLOTS / "memoria.png", dpi=150)
    plt.close(fig)


def main() -> None:
    PLOTS.mkdir(parents=True, exist_ok=True)
    rows = load_summary()
    plot_compression_ratio(rows)
    plot_execution_time(rows)
    plot_memory(rows)
    print(f"Graficos salvos em {PLOTS}")


if __name__ == "__main__":
    main()
