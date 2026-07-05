import struct
from typing import List, Tuple

LZW_MAGIC = b"LZW1"
INITIAL_DICT_SIZE = 256
MAX_DICT_SIZE = 4096
MIN_CODE_WIDTH = 9
MAX_CODE_WIDTH = 12


def _code_width(dict_size: int) -> int:
    width = MIN_CODE_WIDTH
    threshold = 1 << width
    while dict_size >= threshold and width < MAX_CODE_WIDTH:
        width += 1
        threshold = 1 << width
    return width


def encode(data: bytes) -> bytes:
    dictionary = {bytes([i]): i for i in range(INITIAL_DICT_SIZE)}
    next_code = INITIAL_DICT_SIZE
    codes: List[int] = []

    if not data:
        return LZW_MAGIC + struct.pack(">I", 0)

    w = bytes([data[0]])
    for i in range(1, len(data)):
        c = bytes([data[i]])
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            codes.append(dictionary[w])
            if next_code < MAX_DICT_SIZE:
                dictionary[wc] = next_code
                next_code += 1
            w = c

    codes.append(dictionary[w])

    body = bytearray(LZW_MAGIC)
    body.extend(struct.pack(">I", len(codes)))
    for code in codes:
        body.extend(struct.pack(">H", code))
    return bytes(body)


def decode(data: bytes) -> bytes:
    if not data.startswith(LZW_MAGIC):
        raise ValueError("Arquivo LZW invalido")

    offset = len(LZW_MAGIC)
    num_codes = struct.unpack_from(">I", data, offset)[0]
    offset += 4

    codes: List[int] = []
    for _ in range(num_codes):
        code = struct.unpack_from(">H", data, offset)[0]
        offset += 2
        codes.append(code)

    dictionary = {i: bytes([i]) for i in range(INITIAL_DICT_SIZE)}
    next_code = INITIAL_DICT_SIZE

    if not codes:
        return b""

    result = bytearray(dictionary[codes[0]])
    prev = codes[0]

    for code in codes[1:]:
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = dictionary[prev] + bytes([dictionary[prev][0]])
        else:
            raise ValueError(f"Codigo LZW invalido: {code}")

        result.extend(entry)

        if next_code < MAX_DICT_SIZE:
            dictionary[next_code] = dictionary[prev] + bytes([entry[0]])
            next_code += 1

        prev = code

    return bytes(result)
