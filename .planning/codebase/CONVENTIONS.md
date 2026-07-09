# Coding Conventions

**Analysis Date:** 2026-07-09

## Naming Patterns

**Files:**
- Snake case: `encoder.py`, `decoder.py`, `bitstream.py`, `metrics.py`
- Module-level organization: One primary class or function per file when possible
- Dual responsibility files group related encode/decode in modules under dedicated directories

**Functions:**
- Snake case for all functions: `build_frequency_table()`, `generate_codes()`, `measure_compression()`
- Private/internal functions prefixed with underscore: `_code_width()` in `src/lzw/encoder.py`
- Verb-first naming for actions: `encode()`, `decode()`, `analyze_file()`, `collect_files()`

**Variables:**
- Snake case for all local and instance variables: `frequencies`, `original_size`, `bitstream`, `result`
- Underscore prefix for private attributes: `_buffer`, `_current`, `_bits_in_current` in `BitWriter`
- Abbreviations acceptable in context: `wc` (word+char combination in `src/lzw/encoder.py:31`)

**Types:**
- PascalCase for all class names: `BitWriter`, `BitReader`, `HuffmanNode`, `CompressionResult`, `FileProfile`
- Private/internal classes prefixed with underscore: `_QueueItem` in `src/huffman/tree.py:7`
- Dataclass decorators used without modification: `@dataclass`, `@dataclass(order=True)`

**Constants:**
- UPPER_CASE for module-level constants: `HUFFMAN_MAGIC = b"HUF1"` in `src/huffman/encoder.py:7`
- Constants placed at module top level, before functions and classes

## Code Style

**Formatting:**
- No explicit formatter configured (no `.prettierrc`, `black.toml`, or `pyproject.toml`)
- Observed style follows PEP 8 conventions
- Line length appears consistent but not enforced (typical ~100 chars)
- Blank lines separate logical sections within functions
- Two blank lines between module-level definitions

**Linting:**
- No linting configuration files present (no `.flake8`, `.pylintrc`, `pyproject.toml`)
- Style inferred from existing code patterns
- Type hints enforced by convention, not by tooling

## Import Organization

**Order:**
1. Standard library imports: `import struct`, `import time`, `import hashlib`
2. Third-party imports: `import pytest`, `from dataclasses import dataclass`
3. Relative project imports: `from src.huffman.tree import build_frequency_table`

**Path Aliases:**
- No path aliases configured
- Absolute imports from project root: `from src.huffman.decoder import decode as huffman_decode`
- Aliasing used for disambiguation: `from src.huffman.decoder import decode as huffman_decode` vs `from src.lzw.decoder import decode as lzw_decode` in `src/benchmark/compare.py:9-15`

## Error Handling

**Patterns:**
- Explicit exception types: `ValueError` for invalid data formats, `EOFError` for bitstream exhaustion
- Error messages in Portuguese mixed with English: `"Arquivo Huffman invalido"`, `"Fim do bitstream atingido"`
- Validation at function entry: `if not data.startswith(HUFFMAN_MAGIC): raise ValueError(...)` in `src/huffman/decoder.py:11-12`
- No try-except blocks in core algorithm code; validation delegates responsibility to caller

## Logging

**Framework:** None — uses direct exception raising and console output

**Patterns:**
- No logger configured; errors surface as exceptions
- Output via `print()` statements in CLI entry points: `print(f"Benchmark concluido: {len(rows)} registros...")` in `src/benchmark/compare.py:104`
- Return codes signal execution status: `return 0` in `src/benchmark/compare.py:105`

## Comments

**When to Comment:**
- Minimal inline comments; code clarity preferred through naming and type hints
- Algorithm-specific logic documented implicitly through variable names and control flow
- No docstrings observed (functions rely on type hints for interface clarity)

**JSDoc/TSDoc:**
- Not applicable (Python project)
- No Google-style or NumPy-style docstrings used

## Function Design

**Size:** Functions are generally compact (5-50 lines), with clear single responsibility:
- `build_frequency_table()` (5 lines) - counts byte frequencies
- `generate_codes()` (9 lines) - recursively generates Huffman codes
- `measure_compression()` (27 lines) - comprehensive compression measurement

**Parameters:**
- Type hints on all parameters: `def encode(data: bytes) -> bytes:`
- Parameters kept minimal; complex state bundled into dataclasses
- Positional arguments only; no keyword-only arguments observed

**Return Values:**
- Explicit return types: `-> bytes`, `-> Dict[int, int]`, `-> CompressionResult`
- Functions return new objects, not mutate inputs (functional style)
- Multiple returns via tuple: `return bytes(self._buffer), padding` in `src/io/bitstream.py:32`

## Module Design

**Exports:**
- Explicit function imports in `__init__.py` files (checked `src/huffman/__init__.py` - empty)
- No barrel file pattern; consumers import directly from module paths
- Example: `from src.huffman.encoder import encode as huffman_encode` rather than `from src.huffman import encode`

**Barrel Files:**
- Not used; each module maintains internal cohesion without re-exports
- Simplifies dependency tracking and circular import prevention

---

*Convention analysis: 2026-07-09*
