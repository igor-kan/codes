/**
 * Huffman Coding (CLRS 3rd Ed. Chapter 16.3)
 * Optimal prefix-free binary character encoding using priority queues.
 */

class HNode {
  char: string | null;
  freq: number;
  left: HNode | null = null;
  right: HNode | null = null;

  constructor(char: string | null, freq: number) {
    this.char = char;
    this.freq = freq;
  }
}

export function buildHuffmanTree(frequencies: Map<string, number>): Map<string, string> {
  const nodes: HNode[] = [];
  for (const [char, freq] of frequencies.entries()) {
    nodes.push(new HNode(char, freq));
  }

  while (nodes.length > 1) {
    nodes.sort((a, b) => a.freq - b.freq);
    const left = nodes.shift()!;
    const right = nodes.shift()!;
    const parent = new HNode(null, left.freq + right.freq);
    parent.left = left;
    parent.right = right;
    nodes.push(parent);
  }

  const root = nodes[0];
  const codes = new Map<string, string>();

  function generateCodes(node: HNode | null, current: string): void {
    if (!node) return;
    if (node.char !== null) {
      codes.set(node.char, current || "0");
      return;
    }
    generateCodes(node.left, current + "0");
    generateCodes(node.right, current + "1");
  }

  generateCodes(root, "");
  return codes;
}

const freqMap = new Map([
  ["a", 45],
  ["b", 13],
  ["c", 12],
  ["d", 16],
  ["e", 9],
  ["f", 5],
]);
const hCodes = buildHuffmanTree(freqMap);
if (!hCodes.has("a") || hCodes.get("a")!.length !== 1) {
  throw new Error("Huffman Coding verification failed");
}
console.log("CLRS Huffman Coding verified successfully.");
