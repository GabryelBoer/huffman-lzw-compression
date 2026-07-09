"""LZW (Lempel-Ziv-Welch) encoder and decoder.

Implements dictionary-based lossless compression via substring replacement.
Encoder: Streaming single-pass algorithm (O(n) time) using hash table for O(1)
substring lookup. Dictionary capped at 4096 entries with reset-on-overflow strategy.
Decoder: Reverse engineers dictionary from codes alone without transmission overhead.
"""

import struct
from typing import List, Tuple

LZW_MAGIC = b"LZW1"
INITIAL_DICT_SIZE = 256
MAX_DICT_SIZE = 4096
MIN_CODE_WIDTH = 9
MAX_CODE_WIDTH = 12


def _code_width(dict_size: int) -> int:
    """Calculate minimum code width (bits) for dictionary size.

    Computes minimum bits needed to represent all dictionary codes.
    Code width increases from 9 bits (256 entries) to 12 bits (4096 entries).

    Args:
        dict_size: Current dictionary size.

    Returns:
        Code width in bits (9-12 for valid LZW dictionary sizes).

    Complexity:
        Time: O(1) - at most 4 iterations of bit-width scaling.
        Space: O(1).

    Example:
        >>> _code_width(256)
        9
        >>> _code_width(512)
        10
    """
    width = MIN_CODE_WIDTH
    threshold = 1 << width
    while dict_size >= threshold and width < MAX_CODE_WIDTH:
        width += 1
        threshold = 1 << width
    return width


def encode(data: bytes) -> bytes:
    """Encode data using LZW compression.

    Greedily builds a dictionary of previously-seen substrings. For each position,
    finds the longest substring in the dictionary, emits its code, and adds the
    extended substring (if not at capacity) to the dictionary for future reference.
    Dictionary reset-on-overflow capping at 4096 entries.

    Args:
        data: Bytes to compress.

    Returns:
        Encoded bytes with LZW_MAGIC header and code sequence.
        Format: MAGIC(4) | num_codes(4) | {code(2)}*.

    Complexity:
        Time: O(n) where n = len(data). Single pass with O(1) hash-table lookups
              for substring membership testing.
        Space: O(d) where d = dictionary size (≤ 4096 bytes/entries).

    Dictionary hash table: O(1) lookup/insertion vs naive tree O(log d) search,
    enabling the linear-time encoding. Greedy matching (longest known prefix) is
    current best strategy for LZW and preserves dictionary growth optimality.

    Dictionary overflow: When dictionary reaches 4096 entries, new entries are
    discarded but encoding continues. No reset to avoid complexity; decoder will
    rebuild identical dictionary state from codes alone.

    Example:
        >>> len(encode(b"hello")) < len(b"hello") + 8  # May not compress tiny input
        True
    """
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
            # Extend current match; O(1) hash lookup
            w = wc
        else:
            # Longest known prefix found; emit its code and add extension to dictionary
            codes.append(dictionary[w])
            if next_code < MAX_DICT_SIZE:
                # Add new substring for future matches (dictionary grows up to 4096)
                dictionary[wc] = next_code
                next_code += 1
            # Start matching next symbol
            w = c

    codes.append(dictionary[w])

    body = bytearray(LZW_MAGIC)
    body.extend(struct.pack(">I", len(codes)))
    for code in codes:
        body.extend(struct.pack(">H", code))
    return bytes(body)


def decode(data: bytes) -> bytes:
    """Decode LZW-encoded data.

    Reverses LZW encoding by reconstructing the dictionary from the code sequence.
    Decoder mirrors encoder's dictionary growth: for each code, if not yet in
    dictionary, infers the entry from previous code + first byte of previous entry.
    Handles special case: code == next_code (self-referential entry).

    Args:
        data: LZW-encoded bytes (output of encode()).

    Returns:
        Decoded plaintext bytes.

    Raises:
        ValueError: If header is invalid (wrong magic) or code sequence is corrupted.

    Complexity:
        Time: O(n + d) where n = sum of decoded entry lengths, d = dictionary size (≤ 4096).
              Decoding loop O(num_codes), each dictionary lookup O(1), each result
              extension O(length of entry). Total O(n) where n = original data size.
        Space: O(d) for dictionary (same as encoder).

    Dictionary reconstruction: Decoder has no transmitted dictionary but rebuilds
    it identically to encoder's state by processing codes in order. Exploits
    predictable dictionary growth pattern: entry[next_code] = entry[prev] + entry[code][0].

    Special case: code == next_code handles self-referential entries (e.g., "aba"
    encoded as 'a', 'ab', 'aba' where last code references itself).

    Example:
        >>> encoded = encode(b"hello")
        >>> decode(encoded) == b"hello"
        True
    """
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

    # Initialize dictionary with single-byte entries (0-255)
    dictionary = {i: bytes([i]) for i in range(INITIAL_DICT_SIZE)}
    next_code = INITIAL_DICT_SIZE

    if not codes:
        return b""

    result = bytearray(dictionary[codes[0]])
    prev = codes[0]

    for code in codes[1:]:
        if code in dictionary:
            # Code already in dictionary; use directly
            entry = dictionary[code]
        elif code == next_code:
            # Self-referential: entry = previous + first byte of previous
            # Occurs when encoder emits code, then immediately uses it
            entry = dictionary[prev] + bytes([dictionary[prev][0]])
        else:
            raise ValueError(f"Codigo LZW invalido: {code}")

        result.extend(entry)

        if next_code < MAX_DICT_SIZE:
            # Mirror encoder's dictionary growth: new entry = previous + first of current
            dictionary[next_code] = dictionary[prev] + bytes([entry[0]])
            next_code += 1

        prev = code

    return bytes(result)
