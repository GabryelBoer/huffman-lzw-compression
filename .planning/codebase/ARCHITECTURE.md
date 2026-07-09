# Architecture

**Analysis Date:** 2026-07-09

## System Overview

This is a lossless compression comparison framework comparing two algorithms (Huffman and LZW) on source code files. The system is organized into three logical layers: compression algorithms, infrastructure (I/O), and analysis/benchmarking.

```text
┌──────────────────────────────────────────────────────────────┐
│          Benchmark & Analysis Layer (Orchestration)          │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ compare.py: Runs benchmark, writes CSV results         │  │
│  │ metrics.py: Measures performance (time, memory, SHA256) │  │
│  │ profile.py: Analyzes file characteristics (entropy)     │  │
│  └────────────────────────────────────────────────────────┘  │
│  `src/benchmark/` — Test harness and analysis               │
├──────────────────────────────────────────────────────────────┤
│       Compression Algorithm Layer (Algorithm Implementation)  │
│  ┌──────────────────┐          ┌──────────────────┐         │
│  │   Huffman Codec  │          │    LZW Codec     │         │
│  │  encoder.py      │          │  encoder.py      │         │
│  │  decoder.py      │          │  decoder.py      │         │
│  │  tree.py         │          │  (dict-based)    │         │
│  │  (heap + tree)   │          │                  │         │
│  └──────────────────┘          └──────────────────┘         │
│  `src/huffman/` and `src/lzw/` — Independent codec pairs    │
├──────────────────────────────────────────────────────────────┤
│           I/O Infrastructure Layer (Bit-Level Operations)    │
│  ┌────────────────────────────────────────────────────────┐  │
│  │ bitstream.py: BitWriter/BitReader for sub-byte ops    │  │
│  └────────────────────────────────────────────────────────┘  │
│  `src/io/bitstream.py` — Bit-level serialization           │
├──────────────────────────────────────────────────────────────┤
│            Input Data & Test Files (External Resources)      │
│  data/codigo/{py,c}/  — Source code files                   │
│  data/baseline/       — Baseline logs for comparison         │
└──────────────────────────────────────────────────────────────┘
```

## Component Responsibilities

| Component | Responsibility | File |
|-----------|----------------|------|
| **Huffman Codec** | Encode/decode using variable-length prefix codes based on frequency analysis | `src/huffman/encoder.py`, `src/huffman/decoder.py` |
| **Huffman Tree** | Build frequency table, construct Huffman tree (min-heap), generate codes | `src/huffman/tree.py` |
| **LZW Codec** | Encode/decode using dictionary-based substitution (code 256-4096) | `src/lzw/encoder.py`, `src/lzw/decoder.py` |
| **BitStream** | Sub-byte read/write operations, padding management | `src/io/bitstream.py` |
| **Benchmark Harness** | Collect files, run both algorithms, write CSV results | `src/benchmark/compare.py` |
| **Metrics** | Time compression/decompression, measure peak memory, validate with SHA-256 | `src/benchmark/metrics.py` |
| **File Profiler** | Compute Shannon entropy, lexical token density, categorize by file type | `src/benchmark/profile.py` |
| **Visualization** | Plot compression ratios, execution time, memory usage | `plot-results.py` |
| **Tests** | Round-trip compression/decompression validation | `tests/test_roundtrip.py` |

## Pattern Overview

**Overall:** Two-phase compression benchmarking system

**Key Characteristics:**
- **Encoder/decoder symmetry**: Both algorithms export `encode(bytes) -> bytes` and `decode(bytes) -> bytes` with magic bytes and headers for format validation
- **Pluggable metrics**: Compression, decompression timing, memory profiling, and SHA-256 validation done generically (not algorithm-specific)
- **File categorization**: Profiler detects `.py`, `.c`, and `.log` files and assigns categories (e.g., `py_alta_entropia`, `c_medio`, `baseline_log`)
- **CSV-driven results**: All metrics output to structured CSV for downstream analysis

## Layers

**Compression Codec Layer:**
- Purpose: Implement lossless compression via two different algorithms
- Location: `src/huffman/`, `src/lzw/`
- Contains: Encoder and decoder functions, data structures (trees, dictionaries)
- Depends on: `src/io/bitstream.py` (for Huffman), struct (for headers)
- Used by: `src/benchmark/compare.py` (via function references passed to measure_compression)

**I/O Infrastructure Layer:**
- Purpose: Provide bit-level read/write operations (Huffman requires this; LZW uses byte-level struct packing)
- Location: `src/io/bitstream.py`
- Contains: `BitWriter` class (accumulates bits, flushes to bytes with padding info), `BitReader` class (reads bits from padded byte stream)
- Depends on: struct (for utilities)
- Used by: `src/huffman/encoder.py`, `src/huffman/decoder.py`

**Analysis & Benchmarking Layer:**
- Purpose: Orchestrate test runs, measure performance, analyze file characteristics
- Location: `src/benchmark/`
- Contains:
  - `compare.py`: Entry point; collects files, runs both algorithms, builds summary/detail CSVs
  - `metrics.py`: `CompressionResult` dataclass, `measure_compression()` function with tracemalloc for memory
  - `profile.py`: `FileProfile` dataclass, Shannon entropy, lexical token pattern analysis, file classification
- Depends on: Huffman and LZW codec pairs (imported as functions)
- Used by: Command-line invocation via `python -m src.benchmark.compare` (in `run-all.sh`)

**Visualization Layer:**
- Purpose: Convert CSV results to PNG plots
- Location: `plot-results.py` (top-level script, not in src/)
- Contains: Three plotting functions (compression ratio, execution time, memory)
- Depends on: CSV results from `src/benchmark/compare`
- Used by: `run-all.sh` (second command)

**Test Layer:**
- Purpose: Validate round-trip fidelity (compress → decompress == original)
- Location: `tests/test_roundtrip.py`
- Contains: Parametrized pytest tests for both Huffman and LZW
- Depends on: Both codec pairs
- Invoked by: pytest (via `pytest tests/`)

## Data Flow

### Primary Benchmark Path

1. **Start**: `bash run-all.sh` sets `PYTHONPATH` and invokes compare module
2. **File Discovery** (`compare.py:collect_files()`): Recursively scan `data/` for `.py`, `.c`, `.log` files
3. **Per-File Processing** (`compare.py:run_benchmark()`):
   - Read file bytes
   - Analyze with `profile.analyze_file()` → Shannon entropy, token density, category
   - For each algorithm (Huffman, LZW):
     - Call `measure_compression(algorithm, data, compress_fn, decompress_fn)`
     - Timing (tracemalloc): compress, then decompress in separate traced sessions
     - SHA-256 validation of round-trip
     - Results → `CompressionResult` dataclass
   - Build row dict via `result_to_row()`, append to summary and detail lists
4. **Output**: Write CSV files
   - `results/compression-summary.csv`: All results aggregated
   - `results/compression-detail-{filename}.csv`: Per-file detail
5. **Visualization** (`plot-results.py`): Load CSV, extract metric columns, plot three bar charts → `benchmark-plots/*.png`

**State Management:**
- No persistent state across runs
- All state is local to function scope (frequencies, dictionaries, bitstreams)
- CSV output is the only artifact that persists between benchmark and visualization

## Key Abstractions

**HuffmanNode:**
- Purpose: Tree node in Huffman coding tree
- Examples: `src/huffman/tree.py` (lines 13-17)
- Pattern: Dataclass with weight, optional symbol (for leaf), optional left/right children

**BitWriter / BitReader:**
- Purpose: Sub-byte bit-level I/O (Huffman encodes variable-length bit sequences)
- Examples: `src/io/bitstream.py`
- Pattern: Stateful classes that maintain byte accumulator (BitWriter) or byte+bit index (BitReader)

**CompressionResult:**
- Purpose: Immutable container for all metrics of a single compress/decompress pair
- Examples: `src/benchmark/metrics.py` (lines 8-19)
- Pattern: Dataclass with 10 fields (algorithm, sizes, ratios, times, memory, SHA match)

**FileProfile:**
- Purpose: Immutable characterization of input file (entropy, tokens, category)
- Examples: `src/benchmark/profile.py` (lines 18-24)
- Pattern: Dataclass with 5 fields (entropy, unique_bytes, repetition_rate, token_density, category)

## Entry Points

**CLI Entry (Benchmark):**
- Location: `src/benchmark/compare.py:main()`
- Triggers: `python -m src.benchmark.compare [--input DIR] [--output DIR]`
- Responsibilities: Parse args, compute PROJECT_ROOT for path resolution, call `run_benchmark()`, print status

**Visualization Entry:**
- Location: `plot-results.py:main()`
- Triggers: `python plot-results.py` (standalone)
- Responsibilities: Load CSV from `results/compression-summary.csv`, call three plot functions, write PNGs

**Test Entry:**
- Location: `tests/test_roundtrip.py` (pytest collected)
- Triggers: `pytest tests/`
- Responsibilities: Parametrized tests validate codec fidelity on diverse inputs

## Architectural Constraints

- **Algorithm isolation**: Huffman and LZW are completely independent; no shared state or coupling
- **Magic bytes for format validation**: Each codec writes a 4-byte magic header (`HUF1` for Huffman, `LZW1` for LZW) to distinguish compressed output
- **Fixed dictionary size (LZW)**: Maximum 4096 codes (12-bit codes); when exceeded, encoder stops adding and uses existing dictionary
- **Padding tracking (Huffman)**: BitWriter tracks padding bits (0-7) on flush; BitReader uses this to know when to stop reading bits
- **No circular imports**: Benchmark imports both codecs; codecs only import from `io/` and stdlib
- **Python 3.11+**: Type hints throughout; uses dataclasses and modern f-strings (requires modern Python)
- **Global state**: None. All state is local to function calls or class instances.

## Error Handling

**Strategy:** Fail-fast with descriptive exceptions

**Patterns:**
- Invalid format detection: Decode functions check magic bytes first (e.g., `if not data.startswith(HUFFMAN_MAGIC)`)
- Bitstream exhaustion: `BitReader.read_bits()` raises `EOFError` if read beyond bounds
- Corrupt data: LZW decoder checks for invalid code values; Huffman checks for None node traversal
- File errors: `FileNotFoundError` if input directory has no matching files

## Cross-Cutting Concerns

**Logging:** Only print statements for user feedback; no structured logging framework
- `compare.py` prints benchmark completion message
- `plot-results.py` prints output path

**Validation:** 
- Round-trip SHA-256 validation (in `measure_compression()`)
- Magic byte checks on decode (in both `huffman/decoder.py` and `lzw/encoder.py`)

**Authentication:** Not applicable (no external services)

---

*Architecture analysis: 2026-07-09*
