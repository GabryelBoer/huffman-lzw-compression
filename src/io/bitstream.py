import struct
from typing import List


class BitWriter:
    def __init__(self) -> None:
        self._buffer = bytearray()
        self._current = 0
        self._bits_in_current = 0

    def write_bits(self, value: int, num_bits: int) -> None:
        for i in range(num_bits - 1, -1, -1):
            bit = (value >> i) & 1
            self._current = (self._current << 1) | bit
            self._bits_in_current += 1
            if self._bits_in_current == 8:
                self._buffer.append(self._current)
                self._current = 0
                self._bits_in_current = 0

    def write_code(self, value: int, width: int) -> None:
        self.write_bits(value, width)

    def flush(self) -> bytes:
        padding = 0
        if self._bits_in_current > 0:
            self._current <<= 8 - self._bits_in_current
            self._buffer.append(self._current)
            padding = 8 - self._bits_in_current
            self._current = 0
            self._bits_in_current = 0
        return bytes(self._buffer), padding

    @property
    def byte_count(self) -> int:
        return len(self._buffer) + (1 if self._bits_in_current > 0 else 0)


class BitReader:
    def __init__(self, data: bytes, padding: int = 0) -> None:
        self._data = data
        self._byte_index = 0
        self._bit_index = 0
        self._padding = padding
        self._total_bits = len(data) * 8 - padding

    def read_bits(self, num_bits: int) -> int:
        value = 0
        for _ in range(num_bits):
            if self._byte_index * 8 + self._bit_index >= self._total_bits:
                raise EOFError("Fim do bitstream atingido")
            byte = self._data[self._byte_index]
            bit = (byte >> (7 - self._bit_index)) & 1
            value = (value << 1) | bit
            self._bit_index += 1
            if self._bit_index == 8:
                self._bit_index = 0
                self._byte_index += 1
        return value

    def read_code(self, width: int) -> int:
        return self.read_bits(width)

    @property
    def exhausted(self) -> bool:
        return self._byte_index * 8 + self._bit_index >= self._total_bits


def write_uint32_list(values: List[int]) -> bytes:
    return struct.pack(f">{len(values)}I", *values)


def read_uint32_list(data: bytes, count: int) -> List[int]:
    return list(struct.unpack(f">{count}I", data[: count * 4]))
