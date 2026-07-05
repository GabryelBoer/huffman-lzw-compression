import argparse
import csv
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.benchmark.metrics import CompressionResult, measure_compression
from src.benchmark.profile import FileProfile, analyze_file
from src.huffman.decoder import decode as huffman_decode
from src.huffman.encoder import encode as huffman_encode
from src.lzw.decoder import decode as lzw_decode
from src.lzw.encoder import encode as lzw_encode


def collect_files(input_dir: Path) -> list[Path]:
    extensions = {".py", ".c", ".log"}
    files = []
    for path in sorted(input_dir.rglob("*")):
        if path.is_file() and path.suffix.lower() in extensions:
            files.append(path)
    return files


def write_summary_csv(path: Path, rows: list[dict]) -> None:
    if not rows:
        return
    fieldnames = list(rows[0].keys())
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def result_to_row(
    file_path: Path,
    profile: FileProfile,
    result: CompressionResult,
) -> dict:
    return {
        "arquivo": file_path.name,
        "categoria": profile.category,
        "algoritmo": result.algorithm,
        "tamanho_original_bytes": result.original_size,
        "tamanho_comprimido_bytes": result.compressed_size,
        "taxa_compressao": round(result.compression_ratio, 4),
        "fator_compressao": round(result.compression_factor, 4),
        "percentual_economizado": round(result.saving_percent, 2),
        "tempo_compressao_ms": round(result.compress_time_ms, 3),
        "tempo_descompressao_ms": round(result.decompress_time_ms, 3),
        "memoria_pico_kb": round(result.peak_memory_kb, 2),
        "entropia_shannon": round(profile.entropy, 4),
        "taxa_repeticao_lexical": round(profile.lexical_repetition_rate, 4),
        "densidade_tokens": round(profile.token_density, 4),
        "lossless_ok": result.sha256_match,
    }


def run_benchmark(input_dir: Path, output_dir: Path) -> list[dict]:
    output_dir.mkdir(parents=True, exist_ok=True)
    files = collect_files(input_dir)
    if not files:
        raise FileNotFoundError(f"Nenhum arquivo encontrado em {input_dir}")

    summary_rows: list[dict] = []

    for file_path in files:
        data = file_path.read_bytes()
        profile = analyze_file(file_path.name, data)
        detail_rows = []

        for algorithm, compress_fn, decompress_fn in (
            ("Huffman", huffman_encode, huffman_decode),
            ("LZW", lzw_encode, lzw_decode),
        ):
            result = measure_compression(algorithm, data, compress_fn, decompress_fn)
            row = result_to_row(file_path, profile, result)
            summary_rows.append(row)
            detail_rows.append(row)

        detail_path = output_dir / f"compression-detail-{file_path.stem}.csv"
        write_summary_csv(detail_path, detail_rows)

    write_summary_csv(output_dir / "compression-summary.csv", summary_rows)
    return summary_rows


def main() -> int:
    parser = argparse.ArgumentParser(description="Benchmark Huffman vs LZW")
    parser.add_argument("--input", type=Path, default=Path("data/codigo"))
    parser.add_argument("--output", type=Path, default=Path("results"))
    args = parser.parse_args()

    project_root = PROJECT_ROOT
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

    input_dir = args.input if args.input.is_absolute() else project_root / args.input
    output_dir = args.output if args.output.is_absolute() else project_root / args.output

    rows = run_benchmark(input_dir, output_dir)
    print(f"Benchmark concluido: {len(rows)} registros em {output_dir / 'compression-summary.csv'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
