/**
 * @file cache_locality.cpp
 * @brief Memory hierarchy alignment and cacheline optimizations for Canonical Huffman Variable-Length Entropy Codec.
 * Module: huffman_codec
 */

#define HUFFMAN_CODEC_CACHELINE_SIZE 64
#define HUFFMAN_CODEC_BLOCK_SIZE 32

void huffman_codec_cache_blocked_operation(const double* in_mat, double* out_mat, size_t n) {
    for (size_t bi = 0; bi < n; bi += HUFFMAN_CODEC_BLOCK_SIZE) {
        size_t bi_end = (bi + HUFFMAN_CODEC_BLOCK_SIZE < n) ? (bi + HUFFMAN_CODEC_BLOCK_SIZE) : n;
        for (size_t bj = 0; bj < n; bj += HUFFMAN_CODEC_BLOCK_SIZE) {
            size_t bj_end = (bj + HUFFMAN_CODEC_BLOCK_SIZE < n) ? (bj + HUFFMAN_CODEC_BLOCK_SIZE) : n;
            for (size_t i = bi; i < bi_end; ++i) {
                for (size_t j = bj; j < bj_end; ++j) {
                    out_mat[i * n + j] = in_mat[i * n + j] * 1.000001;
                }
            }
        }
    }
}
