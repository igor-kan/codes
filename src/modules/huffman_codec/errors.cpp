/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Canonical Huffman Variable-Length Entropy Codec.
 * Module: huffman_codec
 */

typedef enum huffman_codec_error {
    HUFFMAN_CODEC_SUCCESS = 0,
    HUFFMAN_CODEC_ERR_INVALID_INPUT = -1,
    HUFFMAN_CODEC_ERR_BUFFER_OVERFLOW = -2,
    HUFFMAN_CODEC_ERR_CONVERGENCE_FAIL = -3
} huffman_codec_error_t;

const char* huffman_codec_str_error(huffman_codec_error_t code) {
    switch (code) {
        case HUFFMAN_CODEC_SUCCESS: return "Operation completed successfully";
        case HUFFMAN_CODEC_ERR_INVALID_INPUT: return "Input argument violates domain preconditions";
        case HUFFMAN_CODEC_ERR_BUFFER_OVERFLOW: return "Output buffer capacity exceeded";
        case HUFFMAN_CODEC_ERR_CONVERGENCE_FAIL: return "Numerical algorithm failed to converge within limit";
        default: return "Unrecognized error code";
    }
}
