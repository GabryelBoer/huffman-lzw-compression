# Technology Stack

**Analysis Date:** 2026-07-09

## Languages

**Primary:**
- Python 3.11+ - Core compression algorithms, benchmarking, and analysis

## Runtime

**Environment:**
- Python 3.11+ (verified in README)

**Package Manager:**
- pip
- Lockfile: `.venv/` virtual environment present

## Frameworks

**Core:**
- None - Pure Python standard library for algorithm implementation

**Testing:**
- pytest 8.0.0+ - Parametrized round-trip testing in `tests/test_roundtrip.py`

**Data Analysis & Visualization:**
- matplotlib 3.8.0+ - Plotting compression metrics and performance charts in `plot-results.py`
- numpy 1.26.0+ - Numerical operations for chart generation

**Document Generation:**
- python-docx 1.1.0+ - Word document generation for reports
- fpdf2 2.7.0+ - PDF report generation

## Key Dependencies

**Critical:**
- pytest - Test framework for validation of lossless compression round-trip (encoder → decoder → original data)
- numpy - Array operations for statistical visualization
- matplotlib - Chart rendering for compression ratio, execution time, and memory usage graphs

**Analysis:**
- python-docx - Generate .docx reports with benchmark results and analysis
- fpdf2 - Generate PDF reports from benchmark CSV data

## Configuration

**Environment:**
- Project uses `.venv/` directory for virtual environment isolation
- Python path configured via `export PYTHONPATH="$(pwd)"` in `run-all.sh`

**Build:**
- No build configuration files (pytest.ini, setup.py, pyproject.toml) detected
- Tests run via `pytest` without explicit configuration

## Standard Library Usage

**Core Algorithms:**
- `heapq` - Heap operations for Huffman tree construction in `src/huffman/tree.py`
- `struct` - Binary serialization/deserialization for encoded data headers
- `time` - Performance timing in `src/benchmark/metrics.py` using `time.perf_counter()`
- `tracemalloc` - Memory profiling and peak memory measurement in `src/benchmark/metrics.py`
- `hashlib` - SHA-256 validation for lossless round-trip verification in `src/benchmark/metrics.py`
- `csv` - Results output in `src/benchmark/compare.py` and `plot-results.py`
- `argparse` - CLI argument parsing in `src/benchmark/compare.py`
- `pathlib` - File system operations
- `dataclasses` - Data structure definitions (`CompressionResult`, `FileProfile`, `HuffmanNode`)
- `typing` - Type hints throughout codebase
- `math` - Shannon entropy calculation in `src/benchmark/profile.py`
- `re` - Regular expressions for lexical token analysis in `src/benchmark/profile.py`
- `collections.defaultdict` - Counter operations in `plot-results.py`

## Platform Requirements

**Development:**
- macOS (confirmed in README: "Python 3.14, macOS")
- Standard development environment with Python 3.11+

**Production/Execution:**
- Python 3.11+ with matplotlib backend support
- File system access for reading source code files (.py, .c, .log)
- Output directories: `results/` for CSV, `benchmark-plots/` for PNG images

---

*Stack analysis: 2026-07-09*
