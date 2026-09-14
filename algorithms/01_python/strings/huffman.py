"""Huffman Coding Lossless Data Compression Algorithm.

Builds an optimal prefix code tree using frequency heaps to compress
and decompress arbitrary text data.
"""

import heapq
from collections import Counter
from typing import Dict, Optional, Tuple

class HuffmanNode:
    def __init__(self, char: Optional[str], freq: int, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right

    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.freq < other.freq

def build_huffman_tree(text: str) -> Optional[HuffmanNode]:
    if not text:
        return None
    counts = Counter(text)
    heap: list[HuffmanNode] = [HuffmanNode(c, freq) for c, freq in counts.items()]
    heapq.heapify(heap)

    if len(heap) == 1:
        single = heapq.heappop(heap)
        return HuffmanNode(None, single.freq, left=single)

    while len(heap) > 1:
        n1 = heapq.heappop(heap)
        n2 = heapq.heappop(heap)
        parent = HuffmanNode(None, n1.freq + n2.freq, left=n1, right=n2)
        heapq.heappush(heap, parent)

    return heap[0]

def build_codes(node: Optional[HuffmanNode], prefix: str, code_map: Dict[str, str]):
    if node is None:
        return
    if node.char is not None:
        code_map[node.char] = prefix
        return
    build_codes(node.left, prefix + "0", code_map)
    build_codes(node.right, prefix + "1", code_map)

def encode_huffman(text: str) -> Tuple[str, HuffmanNode]:
    root = build_huffman_tree(text)
    if root is None:
        return "", None
    code_map: Dict[str, str] = {}
    build_codes(root, "", code_map)
    encoded = "".join(code_map[c] for c in text)
    return encoded, root

def decode_huffman(encoded: str, root: Optional[HuffmanNode]) -> str:
    if not encoded or root is None:
        return ""
    decoded = []
    curr = root
    for bit in encoded:
        curr = curr.left if bit == "0" else curr.right
        if curr.char is not None:
            decoded.append(curr.char)
            curr = root
    return "".join(decoded)

if __name__ == "__main__":
    message = "this is an example for a huffman encoding demonstration"
    encoded_bits, tree = encode_huffman(message)
    decoded_message = decode_huffman(encoded_bits, tree)
    assert decoded_message == message
    compression_ratio = (len(encoded_bits) / (len(message) * 8)) * 100
    print(f"[Python Huffman] Decoded message verified.")
    print(f"Original: {len(message)*8} bits, Encoded: {len(encoded_bits)} bits ({compression_ratio:.1f}%)")
