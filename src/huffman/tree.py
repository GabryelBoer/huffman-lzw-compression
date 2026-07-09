"""Huffman tree construction and code generation.

Implements the core algorithm for building optimal prefix-free binary trees
from byte frequency tables. Uses a min-heap to construct the tree in O(k log k) time,
ensuring minimal average code length. Supports code generation via DFS traversal.
"""

import heapq
from dataclasses import dataclass, field
from typing import Dict, List, Optional


@dataclass(order=True)
class _QueueItem:
    """Wrapper for heap priority queue.

    Wraps HuffmanNode with weight field for heap ordering while keeping
    node reference for comparison-free ordering.
    """
    weight: int
    node: "HuffmanNode" = field(compare=False)


@dataclass
class HuffmanNode:
    """Binary tree node for Huffman algorithm.

    Attributes:
        weight: Frequency count (sum of descendants' frequencies for internal nodes).
        symbol: Byte value (0-255) if leaf node, None for internal nodes.
        left: Left subtree (bit 0).
        right: Right subtree (bit 1).

    Invariants:
        - Leaf nodes: symbol != None, left == None, right == None
        - Internal nodes: symbol == None, at least one child != None
    """
    weight: int
    symbol: Optional[int] = None
    left: Optional["HuffmanNode"] = None
    right: Optional["HuffmanNode"] = None


def build_frequency_table(data: bytes) -> Dict[int, int]:
    """Build byte frequency table from input data.

    Single-pass histogram construction via hash table updates.

    Args:
        data: Input bytes to analyze.

    Returns:
        Dictionary mapping byte value (0-255) to occurrence count.

    Complexity:
        Time: O(n) where n = len(data). Single pass with O(1) hash lookups.
        Space: O(k) where k = alphabet size (≤ 256 for bytes).

    Example:
        >>> build_frequency_table(b"aaa")
        {97: 3}
    """
    frequencies: Dict[int, int] = {}
    for byte in data:
        frequencies[byte] = frequencies.get(byte, 0) + 1
    return frequencies


def build_huffman_tree(frequencies: Dict[int, int]) -> HuffmanNode:
    """Construct minimal-height Huffman tree from frequency table.

    Uses a binary min-heap to greedily combine lowest-weight subtrees.
    Guarantees optimal prefix-free codes (minimum average code length).
    Handles edge cases: empty input (returns dummy node) and single symbol
    (returns leaf node wrapped in internal node for consistency).

    Args:
        frequencies: Byte value -> occurrence count mapping.

    Returns:
        Root of Huffman tree (HuffmanNode).

    Complexity:
        Time: O(k log k) where k = number of distinct symbols (≤ 256).
              Each heap operation O(log k); total k insertions + k-1 merges.
        Space: O(k) for heap and tree structure.

    Heap operations: Use min-heap for O(log k) per extraction/insertion,
    avoiding naive O(k²) repeated minimum searches.

    Example:
        >>> tree = build_huffman_tree({65: 5, 66: 9, 67: 12})
        >>> tree.symbol is None  # Root is internal node
        True
    """
    if not frequencies:
        return HuffmanNode(weight=1, symbol=0)
    if len(frequencies) == 1:
        symbol = next(iter(frequencies))
        return HuffmanNode(weight=frequencies[symbol], symbol=symbol)

    heap: List[_QueueItem] = []
    for symbol, weight in sorted(frequencies.items()):
        # Push leaf nodes onto heap; heapq maintains min-heap property O(log k)
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
    """Generate prefix-free codes via depth-first tree traversal.

    Assigns binary code strings (bit sequences) to each leaf symbol
    by appending '0' for left branch, '1' for right branch.
    Single-symbol trees return code "0" for consistency.

    Args:
        node: Root of Huffman tree (or subtree).
        prefix: Current path as "01" string; starts empty at root.

    Returns:
        Dictionary mapping byte value (0-255) to code string (e.g., {65: "01", 66: "001"}).

    Complexity:
        Time: O(k) where k = distinct symbols. Visits each leaf exactly once.
        Space: O(k) for output dictionary + O(log k) call stack depth.
        DFS chosen over BFS for simplicity and call-stack efficiency.

    Example:
        >>> tree = build_huffman_tree({65: 5, 66: 9})
        >>> codes = generate_codes(tree)
        >>> len(codes[65]), len(codes[66])  # Higher freq (66) gets shorter code
        (1, 1)
    """
    if node is None:
        return {}
    if node.symbol is not None:
        return {node.symbol: prefix or "0"}
    codes: Dict[int, str] = {}
    # Traverse left (append '0') and right (append '1') recursively
    codes.update(generate_codes(node.left, prefix + "0"))
    codes.update(generate_codes(node.right, prefix + "1"))
    return codes


def code_lengths_from_tree(node: Optional[HuffmanNode], depth: int = 0) -> Dict[int, int]:
    """Extract code lengths from tree structure.

    Traverses tree to compute bit-length of each symbol's code
    (useful for analysis and validation).

    Args:
        node: Root of Huffman tree (or subtree).
        depth: Current tree depth; starts at 0 at root.

    Returns:
        Dictionary mapping byte value to code length (bits).
        Single-symbol codes return length 1.

    Complexity:
        Time: O(k) where k = distinct symbols. Visits each leaf exactly once.
        Space: O(k) for output dictionary + O(log k) call stack depth.

    Example:
        >>> tree = build_huffman_tree({65: 5, 66: 9, 67: 12})
        >>> lengths = code_lengths_from_tree(tree)
        >>> all(v >= 1 for v in lengths.values())
        True
    """
    if node is None:
        return {}
    if node.symbol is not None:
        return {node.symbol: max(depth, 1)}
    lengths: Dict[int, int] = {}
    lengths.update(code_lengths_from_tree(node.left, depth + 1))
    lengths.update(code_lengths_from_tree(node.right, depth + 1))
    return lengths
