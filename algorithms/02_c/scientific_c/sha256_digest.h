#ifndef SHA256_DIGEST_H
#define SHA256_DIGEST_H

#include <stddef.h>
#include <stdint.h>

void sha256(const uint8_t *data, size_t len, uint8_t hash[32]);

#endif
