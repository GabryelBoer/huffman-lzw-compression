# Codebase Concerns

**Analysis Date:** 2026-07-09

## Tech Debt

**LZW Memory Overhead:**
- Issue: LZW dictionary grows dynamically up to 4096 entries, consuming 5-10x more memory than Huffman (up to 870 KB vs 110 KB)
- Files: `src/lzw/encoder.py`, `src/lzw/decoder.py`
- Impact: Memory-constrained environments (embedded systems, large-scale processing) become problematic. This defeats the purpose of compression in some scenarios.
- Fix approach: Consider implementing a sliding window variant or periodic dictionary reset for streaming compression. Alternatively, expose MAX_DICT_SIZE as a configurable parameter.

**File Expansion with LZW on Certain Inputs:**
- Issue: LZW produces negative compression ratios (expansion) on small files and high-entropy data (encoder_sample.py: -1.61%, high_entropy_payload.py: -33.6%)
- Files: `src/lzw/encoder.py`
- Impact: Using LZW on unsuitable data silently produces larger output without warning. Users may not realize compression failed.
- Fix approach: Add pre-compression check (entropy analysis or trial compression) to detect poor compression candidates. Return an indicator or throw an exception if expansion is detected. Document in API which algorithms are suitable for which data types.

**Hardcoded Algorithm Limits:**
- Issue: MIN_CODE_WIDTH (9) and MAX_CODE_WIDTH (12) are hardcoded constants with no justification or configurability
- Files: `src/lzw/encoder.py` lines 7-8
- Impact: Algorithms are tuned for "medium" files (14-34 KB range). Scaling to very large or very small files requires code modification. No adaptive sizing based on input characteristics.
- Fix approach: Document the rationale for these bounds. Add configuration file or factory parameters to expose tuning. Consider dynamic adjustment based on file size statistics.

**Edge Case in Huffman with Single Symbol:**
- Issue: When input contains only one unique byte, the Huffman tree is built with that symbol as root (line 32 in `src/huffman/tree.py`). The generate_codes function returns `{symbol: "0"}` for this case, but could be problematic if the symbol is 0 itself.
- Files: `src/huffman/tree.py` lines 27-32, 51-55
- Impact: Compression/decompression may work but the code path is untested (no test case for single-byte repeated patterns in `tests/test_roundtrip.py`).
- Fix approach: Add explicit test case with data like `b"\xFF" * 1000`. Verify encoder handles symbol 0 correctly in all tree configurations.

## Known Bugs

**Potential CSV StopIteration in Plotting:**
- Symptoms: `plot-results.py` crashes with StopIteration if CSV rows are malformed or missing expected fields
- Files: `plot-results.py` lines 24-25, 44-45, 64-65 (all use `next()` without default)
- Trigger: Run benchmark with incomplete data, then run `plot-results.py`. If any file is missing an algorithm result, StopIteration is raised.
- Workaround: Ensure benchmark completes fully before plotting. Manually verify `compression-summary.csv` contains all expected (file, algorithm) pairs.

**Bitstream Padding Assumption:**
- Symptoms: BitReader expects padding value to be passed; if wrong padding is used, extra bits may be included in decompression
- Files: `src/io/bitstream.py` lines 40-46, `src/huffman/decoder.py` line 28
- Trigger: Manually construct a Huffman file with incorrect padding value, then decompress
- Workaround: Validate padding value in decoder. Current implementation trusts the stored padding without range checks.

## Security Considerations

**No Input Size Limits:**
- Risk: Compression functions have no maximum input size. A malicious or accidental file of arbitrary size will be loaded entirely into memory.
- Files: `src/huffman/encoder.py` line 11, `src/lzw/encoder.py` line 21
- Current mitigation: Python's memory allocator will eventually fail, but no graceful handling occurs.
- Recommendations: Add MAX_INPUT_SIZE constant (e.g., 1 GB) and raise ValueError if exceeded. Document limit in API.

**Insufficient Magic Number Validation:**
- Risk: Magic numbers (b"HUF1", b"LZW1") are validated but truncated files could cause struct.unpack_from to read beyond bounds
- Files: `src/huffman/decoder.py` lines 11-16, `src/lzw/encoder.py` line 51-56
- Current mitigation: struct.unpack_from will raise struct.error if file is too short, but error message may be cryptic to end users.
- Recommendations: Add explicit length checks before each struct.unpack_from call. Catch struct.error and re-raise with descriptive ValueError.

**Unchecked Data Type Assumptions:**
- Risk: Huffman encoder assumes all bytes in data are valid dict keys in `codes` dict. If tree building is buggy, KeyError could occur, exposing internal state.
- Files: `src/huffman/encoder.py` line 18
- Current mitigation: All bytes in [0, 255] should appear in `codes`, but if an edge case bypasses this, KeyError is uncaught.
- Recommendations: Add assertion that `byte in codes` before accessing. Log or raise descriptive error if a byte is missing.

## Performance Bottlenecks

**O(n²) Complexity in Plotting Functions:**
- Problem: Lines 24-25, 44-45, 64-65 in `plot-results.py` use nested comprehensions with `next(generator expression)` to find matching rows. For N files and M algorithms, this is O(N * M * rows) per plot function.
- Files: `plot-results.py`
- Cause: No indexing; every call to `next()` scans all rows. With 100+ benchmark results, this becomes slow.
- Improvement path: Pre-index rows by (file, algorithm) using a dict or defaultdict. Plotting will become O(N * M). Example: `{(row["arquivo"], row["algoritmo"]): row["taxa_compressao"] for row in rows}`

**Repeated Tree Generation in Huffman:**
- Problem: `generate_codes()` recursively walks the tree for every symbol. With diverse input (256 unique bytes), this can be optimized.
- Files: `src/huffman/tree.py` lines 51-59
- Cause: Called once per compress, but traversal is inherently O(alphabet_size * tree_depth). For a balanced tree, depth is O(log alphabet_size).
- Improvement path: Not critical for current sizes, but consider caching the tree → codes mapping if same trees are built multiple times.

**Memory Tracking Overhead in Benchmarks:**
- Problem: `tracemalloc.start()/stop()` around each compress/decompress call adds overhead. Multiple calls in sequence could skew measurements.
- Files: `src/benchmark/metrics.py` lines 32-44
- Cause: Python's memory tracking incurs 10-40% slowdown depending on system.
- Improvement path: Run measurements in separate processes or use a profiler. For this academic project, acceptable, but document this limitation in RESULTADOS-BENCHMARK.md.

## Fragile Areas

**Huffman Code Generation with Empty Input:**
- Files: `src/huffman/tree.py` lines 27-29, `src/huffman/encoder.py` lines 11-13
- Why fragile: Empty data creates a default tree with symbol=0. generate_codes() then returns `{0: "0"}`. Encoder then attempts to encode empty data by iterating `for byte in data`, which is a no-op. Result is valid but the special case is brittle.
- Safe modification: Test with `b""`, `b"A"`, `b"A" * 256`, and `b"\x00" * 100` to ensure tree edge cases are covered.
- Test coverage: Missing

**LZW Dictionary Reconstruction:**
- Files: `src/lzw/decoder.py` lines 64-87
- Why fragile: Decoder must perfectly reconstruct the encoder's dictionary state. If encoder and decoder diverge (e.g., off-by-one in next_code), silent data corruption occurs.
- Safe modification: Add detailed comments explaining the state transitions. Add assertions (in debug mode) to verify next_code == len(dictionary) at key points.
- Test coverage: Only round-trip validation; no unit tests of dictionary state.

**BitReader Boundary Logic:**
- Files: `src/io/bitstream.py` lines 47-59
- Why fragile: Line 50 uses `>=` comparison with `_total_bits`. If padding is wrong or data is truncated, the boundary check is unreliable.
- Safe modification: Add defensive check: `if self._byte_index >= len(self._data): raise EOFError(...)`. Add logging to diagnose truncation.
- Test coverage: No negative test for truncated data.

## Scaling Limits

**Single-Threaded Processing:**
- Current capacity: Files up to ~100 KB process in <100 ms. Benchmark script processes files sequentially.
- Limit: Large file batches or real-time compression streams require sequential processing time proportional to file count.
- Scaling path: Refactor `run_benchmark()` to use `concurrent.futures.ThreadPoolExecutor` for parallel compression/decompression of different files. Keep single-threaded within-file processing (Huffman and LZW are inherently sequential).

**Memory Usage in LZW:**
- Current capacity: 870 KB dictionary for ~34 KB input.
- Limit: Files >100 MB would require proportionally larger dictionaries, consuming >2 GB+ of memory.
- Scaling path: Implement streaming variant with dictionary reset every N bytes. Or use hybrid: Huffman for compression, LZW only for repetitive patterns detected via entropy sampling.

**CSV Generation and Disk I/O:**
- Current capacity: ~12 benchmark results fit in one CSV file (~2 KB).
- Limit: 1000+ file benchmarks would produce 1000+ CSV detail files. Directory listing becomes slow.
- Scaling path: Use SQLite or Parquet format for structured results. Or aggregate all results in a single database, indexed by file and algorithm.

## Dependencies at Risk

**Deprecated scipy/numpy Usage:**
- Risk: `numpy.arange()` in `plot-results.py` is stable, but matplotlib 3.8+ may deprecate Axes.bar() in future versions.
- Impact: Plotting will break on matplotlib 4.x if API changes.
- Migration plan: Switch to plotly or seaborn for future-proof plotting. Or pin matplotlib to 3.8-3.9 range.

**Python 3.11+ Type Hints:**
- Risk: `list[dict]` syntax in `src/benchmark/compare.py` (line 18) requires Python 3.9+. README claims Python 3.11+, but doesn't enforce it.
- Impact: Code fails silently or with cryptic SyntaxError if run on Python 3.8.
- Migration plan: Add `from __future__ import annotations` to all files using modern hints. Or use `List[Dict[...]]` from typing module for backwards compatibility.

**Unversioned matplotlib:**
- Risk: `requirements.txt` specifies `matplotlib>=3.8.0` with no upper bound. matplotlib 4.0 (expected 2025-2026) may have breaking changes.
- Impact: `pip install -r requirements.txt` on a future system may install incompatible matplotlib.
- Migration plan: Pin to `matplotlib>=3.8.0,<4.0`. Test with latest 3.x before each release.

## Missing Critical Features

**No Streaming API:**
- Problem: All functions are file-in-memory. Cannot compress 1 GB file if RAM is 512 MB.
- Blocks: Real-world adoption for large logs, video preprocessing, or network streaming.

**No Algorithm Selection Helper:**
- Problem: No function to recommend Huffman vs LZW based on input characteristics (entropy, size, repetition).
- Blocks: End users must manually analyze data and choose. High likelihood of wrong choice (as shown in negative compression ratios).

**No Format Version Handling:**
- Problem: Magic numbers b"HUF1" and b"LZW1" are not extensible. Future format changes require breaking compatibility.
- Blocks: Evolving algorithms (e.g., adaptive Huffman) require new magic numbers and manual versioning logic.

## Test Coverage Gaps

**Huffman Encoder with Single-Byte Input:**
- What's not tested: `data = b"A" * 1000` or `data = bytes([0])` (single occurrence of byte 0)
- Files: `tests/test_roundtrip.py` lacks parametrization for single-symbol trees
- Risk: Edge case in `src/huffman/tree.py` line 32 could fail silently
- Priority: High

**LZW Dictionary Boundary Conditions:**
- What's not tested: Input that causes dictionary to reach exactly 4096 entries; input just below/above the threshold
- Files: `tests/test_roundtrip.py` has only 7 data samples; none specifically designed to saturate LZW dict
- Risk: Off-by-one in `next_code < MAX_DICT_SIZE` could cause silent failures
- Priority: High

**Corrupted File Handling:**
- What's not tested: Truncated headers, invalid magic numbers, corrupted bitstreams
- Files: `tests/test_roundtrip.py` only tests valid round-trips
- Risk: Decoders may raise cryptic exceptions or crash instead of returning helpful errors
- Priority: Medium

**Large File Performance:**
- What's not tested: Files >10 MB (beyond range of current benchmark dataset, max 34 KB)
- Files: No performance tests in `tests/`
- Risk: Memory exhaustion or unexpected slowdown not detected until production
- Priority: Medium

**Empty Data Handling:**
- What's tested: `test_roundtrip` includes `b""` (line 16 in `tests/test_roundtrip.py`)
- What's NOT tested: Explicit round-trip of empty data for both Huffman and LZW (both are parametrized, so it should work, but no dedicated test)
- Files: `tests/test_roundtrip.py`
- Risk: Edge case if tree building with empty input regresses
- Priority: Low

**CSV Parsing Robustness:**
- What's not tested: Missing columns, extra columns, malformed floats in `plot-results.py`
- Files: `plot-results.py` lines 14-17
- Risk: StopIteration or KeyError if data is incomplete
- Priority: Medium

---

*Concerns audit: 2026-07-09*
