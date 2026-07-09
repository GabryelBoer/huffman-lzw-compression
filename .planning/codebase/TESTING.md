# Testing Patterns

**Analysis Date:** 2026-07-09

## Test Framework

**Runner:**
- pytest [version from requirements.txt: >=8.0.0]
- Config: No explicit config file; pytest.ini or pyproject.toml not present
- Default pytest behavior applied

**Assertion Library:**
- Built-in Python `assert` statements
- pytest assertions provide rich output for failures

**Run Commands:**
```bash
pytest tests/                  # Run all tests
pytest tests/ -v               # Verbose mode with test names
pytest tests/ --tb=short       # Short traceback format
pytest tests/ -k roundtrip     # Run tests matching pattern
```

## Test File Organization

**Location:**
- Tests co-located in `tests/` directory at project root
- Single test file: `tests/test_roundtrip.py`
- Mirrors the algorithmic structure: tests for both huffman and lzw modules

**Naming:**
- Test file: `test_roundtrip.py` (follows `test_*.py` pytest convention)
- Test functions: `test_huffman_roundtrip()`, `test_lzw_roundtrip()` (prefixed with `test_`)
- Descriptive names indicate purpose: "roundtrip" = compress then decompress and verify

**Structure:**
```
tests/
└── test_roundtrip.py          # All compression codec roundtrip tests
```

## Test Structure

**Suite Organization:**
```python
# From tests/test_roundtrip.py:1-35
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.huffman.decoder import decode as huffman_decode
from src.huffman.encoder import encode as huffman_encode
from src.lzw.decoder import decode as lzw_decode
from src.lzw.encoder import encode as lzw_encode

SAMPLE_TEXTS = [
    b"",
    b"A",
    b"ABABABA",
    b"def import return\n" * 100,
    b"print('hello world')\n" * 50,
    bytes(range(256)),
    open(__file__, "rb").read() if Path(__file__).exists() else b"test",
]

@pytest.mark.parametrize("data", SAMPLE_TEXTS)
def test_huffman_roundtrip(data: bytes) -> None:
    compressed = huffman_encode(data)
    assert huffman_decode(compressed) == data

@pytest.mark.parametrize("data", SAMPLE_TEXTS)
def test_lzw_roundtrip(data: bytes) -> None:
    compressed = lzw_encode(data)
    assert lzw_decode(compressed) == data
```

**Patterns:**
- **Setup pattern:** Direct module imports with explicit aliasing to avoid name collisions (`huffman_encode`, `lzw_encode`)
- **Teardown pattern:** None; tests are stateless with no cleanup needed
- **Assertion pattern:** Simple equality assertion `assert huffman_decode(compressed) == data`
- **Parametrization:** `@pytest.mark.parametrize("data", SAMPLE_TEXTS)` runs each test function once per sample

## Mocking

**Framework:** None used

**Patterns:**
- No mocking library imported or configured
- Tests depend on real encoder/decoder implementations

**What to Mock:**
- File I/O not needed (sample texts created in-memory)
- External dependencies not present in current test suite

**What NOT to Mock:**
- Compression algorithms (core functionality under test)
- Data structures like HuffmanNode (part of the implementation being validated)

## Fixtures and Factories

**Test Data:**
```python
# From tests/test_roundtrip.py:15-23
SAMPLE_TEXTS = [
    b"",                                    # Empty data (edge case)
    b"A",                                   # Single byte
    b"ABABABA",                             # Highly repetitive
    b"def import return\n" * 100,           # Python keywords repeated
    b"print('hello world')\n" * 50,         # Python code repeated
    bytes(range(256)),                      # All byte values (0-255)
    open(__file__, "rb").read() if Path(__file__).exists() else b"test",  # Self-reference test file
]
```

**Location:**
- Module-level constant `SAMPLE_TEXTS` in `tests/test_roundtrip.py`
- Covers edge cases: empty, minimal, repetitive, diverse (all byte values), realistic (source code)
- Self-referential: includes test file contents for realistic compression scenario

## Coverage

**Requirements:** None enforced (no coverage target configured)

**View Coverage:**
```bash
# Would require pytest-cov plugin (not currently in requirements.txt)
pytest tests/ --cov=src --cov-report=html
```

**Current Status:** Coverage monitoring not configured; only roundtrip tests present

## Test Types

**Unit Tests:**
- Not present in current test suite
- Individual functions (`build_frequency_table`, `generate_codes`, etc.) not tested in isolation
- Would benefit from unit tests for edge cases in tree building, code generation

**Integration Tests:**
- `test_huffman_roundtrip()` and `test_lzw_roundtrip()` act as integration tests
- Verify complete compress-decompress cycle for both algorithms
- Validate correctness via data equality (lossless compression)

**E2E Tests:**
- Not present
- Benchmark suite in `src/benchmark/compare.py` serves similar validation role
- Could be formalized with pytest fixtures and file-based tests

## Common Patterns

**Async Testing:**
- Not applicable (synchronous algorithm implementations)

**Error Testing:**
- Not present
- Should test error conditions: invalid compressed data, corrupted headers, truncated streams
- Example missing: `test_huffman_invalid_magic()`, `test_lzw_corrupted_code()`
- Current implementation raises `ValueError` on invalid input, but exceptions not tested

**Parametrized Testing:**
```python
# From tests/test_roundtrip.py:26-29
@pytest.mark.parametrize("data", SAMPLE_TEXTS)
def test_huffman_roundtrip(data: bytes) -> None:
    compressed = huffman_encode(data)
    assert huffman_decode(compressed) == data
```

- Pattern: Single test function runs once per item in `SAMPLE_TEXTS`
- Result: 7 test runs for `test_huffman_roundtrip`, 7 for `test_lzw_roundtrip`
- Total: 14 test cases covering both algorithms

---

*Testing analysis: 2026-07-09*
