/**
 * MurmurHash3 32-bit x86 Implementation.
 * 
 * Why C for this module?
 * C offers direct bitwise manipulation, zero pointer indirection overhead,
 * and compiler-level vectorization, making it the industry standard for
 * low-latency non-cryptographic hashing algorithms (used in Redis, Memcached, Kafka).
 */

#include <stdint.h>
#include <stddef.h>
#include <stdio.h>

static inline uint32_t rotl32(uint32_t x, int8_t r) {
    return (x << r) | (x >> (32 - r));
}

uint32_t murmurhash3_32(const void *key, size_t len, uint32_t seed) {
    const uint8_t *data = (const uint8_t *)key;
    const size_t nblocks = len / 4;
    uint32_t h1 = seed;

    const uint32_t c1 = 0xcc9e2d51;
    const uint32_t c2 = 0x1b873593;

    // Body: Process 32-bit blocks
    const uint32_t *blocks = (const uint32_t *)(data + nblocks * 4);
    for (intptr_t i = -((intptr_t)nblocks); i; i++) {
        uint32_t k1 = blocks[i];

        k1 *= c1;
        k1 = rotl32(k1, 15);
        k1 *= c2;

        h1 ^= k1;
        h1 = rotl32(h1, 13);
        h1 = h1 * 5 + 0xe6546b64;
    }

    // Tail: Process remaining 1..3 bytes
    const uint8_t *tail = (const uint8_t *)(data + nblocks * 4);
    uint32_t k1 = 0;

    switch (len & 3) {
    case 3:
        k1 ^= tail[2] << 16;
    case 2:
        k1 ^= tail[1] << 8;
    case 1:
        k1 ^= tail[0];
        k1 *= c1;
        k1 = rotl32(k1, 15);
        k1 *= c2;
        h1 ^= k1;
    }

    // Finalization avalanche
    h1 ^= len;
    h1 ^= h1 >> 16;
    h1 *= 0x85ebca6b;
    h1 ^= h1 >> 13;
    h1 *= 0xc2b2ae35;
    h1 ^= h1 >> 16;

    return h1;
}

int main(void) {
    const char *key = "quarto-writing-polyglot-vault";
    uint32_t hash = murmurhash3_32(key, 29, 42);
    printf("MurmurHash3-32 of \"%s\" with seed 42 = 0x%08X\n", key, hash);
    return 0;
}
