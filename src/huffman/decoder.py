import struct
from typing import Dict

from src.huffman.tree import build_huffman_tree
from src.io.bitstream import BitReader

HUFFMAN_MAGIC = b"HUF1"


def decode(data: bytes) -> bytes:
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
