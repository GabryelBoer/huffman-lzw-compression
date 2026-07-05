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
