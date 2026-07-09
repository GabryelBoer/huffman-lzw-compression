"""Huffman decoder module.

Reverses Huffman encoding via tree traversal. Reconstructs the frequency table
from the header, rebuilds the identical tree used at encoding time, then traverses
the tree bit-by-bit to recover original data. Stateless: decoder needs no prior
knowledge of the input alphabet or frequencies.
"""

import struct
from typing import Dict

from src.huffman.tree import build_huffman_tree
from src.io.bitstream import BitReader

HUFFMAN_MAGIC = b"HUF1"


def decode(data: bytes) -> bytes:
    """Decode Huffman-encoded data.

    Parses header to extract frequency table, reconstructs the encoding tree,
    then traverses tree following encoded bitstream (0 = left, 1 = right) to
    emit original bytes.

    Args:
        data: Huffman-encoded bytes (output of encode()).

    Returns:
        Decoded plaintext bytes.

    Raises:
        ValueError: If header is invalid (wrong magic) or bitstream is corrupted.

    Complexity:
        Time: O(n + k log k) where n = len(data), k = alphabet size.
              Header parsing O(k), tree reconstruction O(k log k) via heap,
              bitstream traversal O(n).
        Space: O(k) for tree and frequency table.

    Tree traversal convention: bit 0 = left child, bit 1 = right child.
    This mirrors the encoding process where generate_codes appends '0' for left,
    '1' for right.

    Example:
        >>> encoded = encode(b"hello")
        >>> decode(encoded) == b"hello"
        True
    """
    if not data.startswith(HUFFMAN_MAGIC):
        raise ValueError("Arquivo Huffman invalido")

    offset = len(HUFFMAN_MAGIC)
    original_size = struct.unpack_from(">I", data, offset)[0]
    offset += 4
    num_symbols = struct.unpack_from(">H", data, offset)[0]
    offset += 2

    frequencies: Dict[int, int] = {}
    for _ in range(num_symbols):
        symbol = data[offset]
        offset += 1
        count = struct.unpack_from(">I", data, offset)[0]
        offset += 4
        frequencies[symbol] = count

    padding = data[offset]
    offset += 1
    bitstream = data[offset:]

    tree = build_huffman_tree(frequencies)
    reader = BitReader(bitstream, padding)

    result = bytearray()
    node = tree
    while len(result) < original_size:
        if node.symbol is not None:
            result.append(node.symbol)
            node = tree
            continue
        bit = reader.read_bits(1)
        node = node.right if bit else node.left
        if node is None:
            raise ValueError("Bitstream Huffman corrompido")

    return bytes(result)
