import hashlib
import time
import tracemalloc
from dataclasses import dataclass
from typing import Callable, Dict


@dataclass
class CompressionResult:
    algorithm: str
    original_size: int
    compressed_size: int
    compression_ratio: float
    compression_factor: float
    saving_percent: float
    compress_time_ms: float
    decompress_time_ms: float
    peak_memory_kb: float
    sha256_match: bool


def sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def measure_compression(
    algorithm: str,
    data: bytes,
    compress_fn: Callable[[bytes], bytes],
    decompress_fn: Callable[[bytes], bytes],
) -> CompressionResult:
    tracemalloc.start()
    start = time.perf_counter()
    compressed = compress_fn(data)
    compress_time_ms = (time.perf_counter() - start) * 1000
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    tracemalloc.start()
    start = time.perf_counter()
    decompressed = decompress_fn(compressed)
    decompress_time_ms = (time.perf_counter() - start) * 1000
    _, peak_decompress = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    original_size = len(data)
    compressed_size = len(compressed)
    ratio = original_size / compressed_size if compressed_size > 0 else 0.0
    factor = compressed_size / original_size if original_size > 0 else 0.0
    saving = ((original_size - compressed_size) / original_size * 100) if original_size > 0 else 0.0

    return CompressionResult(
        algorithm=algorithm,
        original_size=original_size,
        compressed_size=compressed_size,
        compression_ratio=ratio,
        compression_factor=factor,
        saving_percent=saving,
        compress_time_ms=compress_time_ms,
        decompress_time_ms=decompress_time_ms,
        peak_memory_kb=max(peak, peak_decompress) / 1024,
        sha256_match=sha256_hex(data) == sha256_hex(decompressed),
    )
