#include <stdio.h>
#include <string.h>
#include <assert.h>
#include "sha256_digest.h"

int main(void) {
    const char *msg = "abc";
    uint8_t hash[32];
    sha256((const uint8_t *)msg, 3, hash);
    // Standard test vector for "abc": ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad
    assert(hash[0] == 0xba && hash[1] == 0x78 && hash[2] == 0x16);
    printf("test_sha256_digest PASSED\n");
    return 0;
}
