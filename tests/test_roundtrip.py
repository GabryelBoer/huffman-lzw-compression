"""Round-trip validation tests for Huffman and LZW compression.

Validates lossless compression by verifying that compress(data) followed by
decompress() recovers the original data byte-for-byte. Uses comprehensive
test fixtures covering edge cases and real-world patterns:

- Empty data (no bytes)
- Single byte (minimal case)
- Repetitive patterns (best compression opportunity)
- Code samples (mixed entropy, typical payloads)
- High-entropy data (all 256 byte values, worst compression)
- Self-referential Python code (actual test file)

Validation method: Direct byte comparison (equality assertion).
Validation goal: Ensure no data loss in encode/decode cycle.

Test coverage: 7 distinct data patterns × 2 algorithms = 14 test cases.
All tests must PASS before repository is publication-ready.
"""

import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.huffman.decoder import decode as huffman_decode
from src.huffman.encoder import encode as huffman_encode
from src.lzw.decoder import decode as lzw_decode
from src.lzw.encoder import encode as lzw_encode


# Test fixtures covering compression patterns:
# - Empty: Tests edge case handling (no bytes, no patterns).
# - Single byte: Minimal input for header/tree overhead.
# - Repetitive (ABABABA): High-frequency patterns (best for both algorithms).
# - Code patterns (100x, 50x repeats): Typical payload entropy (Huffman: good,
#   LZW: excellent due to substring repetition).
# - All bytes (0-255): Maximum entropy (worst case for compression).
# - Self file: Real Python source code (mixed entropy, metadata patterns).
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
    """Huffman encode/decode roundtrip validation.

    Tests that Huffman compression is lossless: decompress(compress(data)) == data.
    Parametrized over 7 test cases:
    1. Empty data (no bytes)
    2. Single byte (minimal non-empty case)
    3. Repetitive pattern (high-frequency, good compression)
    4. Code sample with repeats (typical mixed entropy)
    5. Code sample with shorter repeats (different entropy profile)
    6. All 256 byte values (high entropy, worst compression)
    7. Python source file (real-world metadata and code patterns)

    Assertion: Decoded output must match input exactly (byte-for-byte equality).
    Failure indicates: Bug in tree construction, code generation, or bit-stream handling.
    """
    compressed = huffman_encode(data)
    assert huffman_decode(compressed) == data


@pytest.mark.parametrize("data", SAMPLE_TEXTS)
def test_lzw_roundtrip(data: bytes) -> None:
    """LZW encode/decode roundtrip validation.

    Tests that LZW compression is lossless: decompress(compress(data)) == data.
    Parametrized over same 7 test cases as Huffman (consistency).

    LZW-specific edge cases:
    - Empty data: Encoder returns magic + count(0), decoder handles gracefully.
    - Single byte: No dictionary growth, direct emit.
    - Repetitive: Dictionary fills quickly, exploits substring patterns.
    - High entropy: Dictionary capped at 4096; no new entries after cap.
    - Self-referential codes (code == next_code): Handled by decoder special case.

    Assertion: Decoded output must match input exactly (byte-for-byte equality).
    Failure indicates: Bug in dictionary management or code emission/parsing.
    """
    compressed = lzw_encode(data)
    assert lzw_decode(compressed) == data
