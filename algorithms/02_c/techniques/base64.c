/* Base64 encoding. */
#include <stdio.h>
#include <string.h>
static const char *B = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";
void encode(const unsigned char *d, int n, char *out) {
    int o = 0;
    for (int i = 0; i < n; i += 3) {
        unsigned v = d[i] << 16;
        int rem = n - i;
        if (rem > 1) v |= d[i + 1] << 8;
        if (rem > 2) v |= d[i + 2];
        out[o++] = B[(v >> 18) & 63];
        out[o++] = B[(v >> 12) & 63];
        out[o++] = rem > 1 ? B[(v >> 6) & 63] : '=';
        out[o++] = rem > 2 ? B[v & 63] : '=';
    }
    out[o] = '\0';
}
int main(void) {
    char out[64];
    encode((const unsigned char *)"foobar", 6, out);
    if (strcmp(out, "Zm9vYmFy")) return 1;
    printf("base64 %s\n", out);
    return 0;
}
