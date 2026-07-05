import heapq
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(order=True)
class _QueueItem:
    weight: int
    node: "HuffmanNode" = field(compare=False)


@dataclass
class HuffmanNode:
    weight: int
    symbol: Optional[int] = None
    left: Optional["HuffmanNode"] = None
    right: Optional["HuffmanNode"] = None


def build_frequency_table(data: bytes) -> Dict[int, int]:
    frequencies: Dict[int, int] = {}
    for byte in data:
        frequencies[byte] = frequencies.get(byte, 0) + 1
    return frequencies


def build_huffman_tree(frequencies: Dict[int, int]) -> HuffmanNode:
    if not frequencies:
        return HuffmanNode(weight=1, symbol=0)
    if len(frequencies) == 1:
        symbol = next(iter(frequencies))
        return HuffmanNode(weight=frequencies[symbol], symbol=symbol)

    heap: List[_QueueItem] = []
    for symbol, weight in sorted(frequencies.items()):
        heapq.heappush(heap, _QueueItem(weight, HuffmanNode(weight=weight, symbol=symbol)))

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        parent = HuffmanNode(
            weight=first.weight + second.weight,
            left=first.node,
            right=second.node,
        )
        heapq.heappush(heap, _QueueItem(parent.weight, parent))

    return heapq.heappop(heap).node


def generate_codes(node: Optional[HuffmanNode], prefix: str = "") -> Dict[int, str]:
    if node is None:
        return {}
    if node.symbol is not None:
        return {node.symbol: prefix or "0"}
    codes: Dict[int, str] = {}
    codes.update(generate_codes(node.left, prefix + "0"))
    codes.update(generate_codes(node.right, prefix + "1"))
    return codes


def code_lengths_from_tree(node: Optional[HuffmanNode], depth: int = 0) -> Dict[int, int]:
    if node is None:
        return {}
    if node.symbol is not None:
        return {node.symbol: max(depth, 1)}
    lengths: Dict[int, int] = {}
    lengths.update(code_lengths_from_tree(node.left, depth + 1))
    lengths.update(code_lengths_from_tree(node.right, depth + 1))
    return lengths
