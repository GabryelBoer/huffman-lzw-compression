"""Huffman encoder module.

Implements Huffman coding for lossless data compression via optimal prefix-free codes.
The algorithm operates in four stages: frequency analysis O(n), tree construction O(k log k),
code generation O(k), and data encoding O(n), where n is data length and k is alphabet size.
Produces a binary format with embedded frequency table for decompression.
"""

import struct
from typing import Dict

from src.huffman.tree import build_frequency_table, build_huffman_tree, generate_codes
from src.io.bitstream import BitWriter

HUFFMAN_MAGIC = b"HUF1"


def encode(data: bytes) -> bytes:
    """Encode data using Huffman coding.

    Analyzes byte frequencies, constructs an optimal binary tree, generates
    variable-length codes, and encodes data. Stores the frequency table in
    the output header for stateless decompression.

    Args:
        data: bytes to compress.

    Returns:
        Encoded bytes with HUFFMAN_MAGIC header, frequency table, and bitstream.
        Format: MAGIC(4) | original_size(4) | num_symbols(2) |
                {symbol(1) count(4)}* | padding(1) | bitstream.

    Complexity:
        Time: O(n + k log k) where n = len(data), k = alphabet size (≤ 256).
              Frequency counting O(n), tree construction O(k log k) via heap,
              code generation O(k), encoding O(n).
        Space: O(k) for frequency table and Huffman tree.

    Example:
        >>> encoded = encode(b"hello")
        >>> len(encoded) > len(b"hello")  # Header overhead for small input
        True
    """
    frequencies = build_frequency_table(data)
    tree = build_huffman_tree(frequencies)
    codes = generate_codes(tree)

    writer = BitWriter()
    for byte in data:
        for bit_char in codes[byte]:
            writer.write_bits(int(bit_char), 1)

    bitstream, padding = writer.flush()

    header = bytearray(HUFFMAN_MAGIC)
    header.extend(struct.pack(">I", len(data)))
    header.extend(struct.pack(">H", len(frequencies)))
    for symbol, count in sorted(frequencies.items()):
        header.append(symbol)
        header.extend(struct.pack(">I", count))
    header.append(padding)
    header.extend(bitstream)
    return bytes(header)
