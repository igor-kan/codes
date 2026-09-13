/**
 * Probabilistic Bloom Filter with Double Hashing.
 * 
 * Why TypeScript for this module?
 * TypeScript adds compile-time type safety to client/edge data structures,
 * preventing accidental key mismatches in distributed cache membership testing.
 */

export class BloomFilter {
    private readonly size: number;
    private readonly numHashes: number;
    private readonly bitset: Uint8Array;

    constructor(expectedElements: number, falsePositiveRate: number = 0.01) {
        // Optimal size m = - (n * ln(p)) / (ln(2)^2)
        this.size = Math.ceil(- (expectedElements * Math.log(falsePositiveRate)) / (Math.LN2 * Math.LN2));
        // Optimal hash count k = (m / n) * ln(2)
        this.numHashes = Math.ceil((this.size / expectedElements) * Math.LN2);
        this.bitset = new Uint8Array(Math.ceil(this.size / 8));
    }

    private hash(str: string, seed: number): number {
        let h = seed ^ 0x12345678;
        for (let i = 0; i < str.length; i++) {
            h = Math.imul(h ^ str.charCodeAt(i), 0x5bd1e995);
            h ^= h >>> 15;
        }
        return (h >>> 0) % this.size;
    }

    public add(element: string): void {
        const h1 = this.hash(element, 1);
        const h2 = this.hash(element, 2);
        for (let i = 0; i < this.numHashes; i++) {
            // Kirsch-Mitzenmacher double-hashing: g_i(x) = (h1(x) + i * h2(x)) mod m
            const bitIndex = (h1 + i * h2) % this.size;
            this.setBit(bitIndex);
        }
    }

    public mightContain(element: string): boolean {
        const h1 = this.hash(element, 1);
        const h2 = this.hash(element, 2);
        for (let i = 0; i < this.numHashes; i++) {
            const bitIndex = (h1 + i * h2) % this.size;
            if (!this.getBit(bitIndex)) return false;
        }
        return true;
    }

    private setBit(index: number): void {
        const byteIdx = Math.floor(index / 8);
        const bitIdx = index % 8;
        this.bitset[byteIdx] |= (1 << bitIdx);
    }

    private getBit(index: number): boolean {
        const byteIdx = Math.floor(index / 8);
        const bitIdx = index % 8;
        return (this.bitset[byteIdx] & (1 << bitIdx)) !== 0;
    }
}
