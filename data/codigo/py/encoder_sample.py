import struct
from typing import Dict, Tuple

from src.huffman.tree import build_frequency_table, build_huffman_tree, generate_codes
from src.io.bitstream import BitWriter

HUFFMAN_MAGIC = b"HUF1"


def encode(data: bytes) -> bytes:
    frequencies = build_frequency_table(data)
    tree = build_huffman_tree(frequencies)
    codes = generate_codes(tree)

    writer = BitWriter()
    for byte in data:
        code = codes[byte]
        for bit_char in code:
            writer.write_bits(int(bit_char), 1)

    bitstream, padding = writer.flush()

    header = bytearray(HUFFMAN_MAGIC)
    header.extend(struct.pack(">I", len(data)))
    header.append(len(frequencies))
    for symbol, count in sorted(frequencies.items()):
        header.append(symbol)
        header.extend(struct.pack(">I", count))
    header.append(padding)
    header.extend(bitstream)
    return bytes(header)


def get_code_table(data: bytes) -> Dict[int, str]:
    frequencies = build_frequency_table(data)
    tree = build_huffman_tree(frequencies)
    return generate_codes(tree)
