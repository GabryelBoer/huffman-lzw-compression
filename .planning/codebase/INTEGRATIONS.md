# External Integrations

**Analysis Date:** 2026-07-09

## APIs & External Services

**None detected.**

This project is self-contained and does not integrate with external APIs or cloud services. All processing occurs locally on the developer's machine.

## Data Storage

**Databases:**
- Not used - Project uses local CSV files for results storage

**File Storage:**
- Local filesystem only
- Input files: `data/codigo/` (Python and C source files), `data/baseline/` (log files for baseline comparison)
- Output: `results/` directory with CSV files
- Generated artifacts: `benchmark-plots/` directory with PNG charts

**Caching:**
- Not used - Each benchmark run generates fresh results

## Authentication & Identity

**Auth Provider:**
- Not applicable - No external authentication required

## Monitoring & Observability

**Error Tracking:**
- None configured - Standard Python exception handling

**Logs:**
- Standard output only via `print()` statements in `run-all.sh` and `plot-results.py`
- No structured logging framework

## CI/CD & Deployment

**Hosting:**
- Not applicable - Local research/academic project (UFABC coursework)
- Runs on developer machine via `bash run-all.sh`

**CI Pipeline:**
- Not configured - Manual test execution via pytest

**Version Control:**
- Git repository present (`.git/` directory)
- No automated deployment pipeline

## Environment Configuration

**Required env vars:**
- `PYTHONPATH` - Set dynamically in `run-all.sh` to project root: `export PYTHONPATH="$(pwd)"`

**Secrets location:**
- No secrets in project - No API keys, tokens, or credentials required

## Webhooks & Callbacks

**Incoming:**
- None

**Outgoing:**
- None

## File Format Outputs

**Results Storage:**
- CSV format (via Python `csv.DictWriter`):
  - `results/compression-summary.csv` - Aggregated benchmark results
  - `results/compression-detail-{filename}.csv` - Per-file detailed metrics
  
**Charts:**
- PNG format (via matplotlib):
  - `benchmark-plots/compression-ratio.png` - Bar chart comparing Huffman vs LZW compression ratios
  - `benchmark-plots/tempo-execucao.png` - Bar chart comparing compression/decompression execution time
  - `benchmark-plots/memoria.png` - Bar chart comparing peak memory usage

**Reports:**
- Markdown: `RESULTADOS-BENCHMARK.md` - Detailed analysis document
- Word: `article/artigo.docx` - Research article (excluded from git)
- PDF: Via fpdf2 (not currently used in visible output)

## Test Data

**Input Files:**
- Source code samples: `data/codigo/*.py` and `data/codigo/*.c`
- Baseline: `data/baseline/access.log` (web server log for comparison)
- In-memory test samples: `tests/test_roundtrip.py` uses parametrized test data including empty, single byte, repetitive patterns, and file contents

## Data Flow

```
Input files (.py, .c, .log)
    ↓
src/benchmark/compare.py (orchestration)
    ├─ src/huffman/encoder.py → compressed bytes
    ├─ src/huffman/decoder.py → decompressed bytes
    ├─ src/lzw/encoder.py → compressed bytes
    ├─ src/lzw/decoder.py → decompressed bytes
    ├─ src/benchmark/metrics.py (time, memory, SHA-256 validation)
    └─ src/benchmark/profile.py (entropy, token analysis)
    ↓
results/*.csv (metric storage)
    ↓
plot-results.py (reads CSV)
    ↓
benchmark-plots/*.png (visualization)
```

---

*Integration audit: 2026-07-09*
