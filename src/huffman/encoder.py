import struct
from typing import Dict

from src.huffman.tree import build_frequency_table, build_huffman_tree, generate_codes
from src.io.bitstream import BitWriter

HUFFMAN_MAGIC = b"HUF1"


def encode(data: bytes) -> bytes:
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
