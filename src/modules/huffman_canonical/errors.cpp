/**
 * @file errors.cpp
 * @brief Domain diagnostic error codes and messages for Canonical Huffman Code Table and Decoding Tree.
 * Module: huffman_canonical
 */

typedef enum huffman_canonical_error_status {
    HUFFMAN_CANONICAL_OK = 0,
    HUFFMAN_CANONICAL_ERR_INVALID_PARAM = -10,
    HUFFMAN_CANONICAL_ERR_CAPACITY_LIMIT = -11,
    HUFFMAN_CANONICAL_ERR_NUMERICAL_FAULT = -12
} huffman_canonical_error_status_t;

const char* huffman_canonical_error_string(huffman_canonical_error_status_t err) {
    switch (err) {
        case HUFFMAN_CANONICAL_OK: return "Operational success";
        case HUFFMAN_CANONICAL_ERR_INVALID_PARAM: return "Parameter domain precondition violated";
        case HUFFMAN_CANONICAL_ERR_CAPACITY_LIMIT: return "Buffer capacity boundary reached";
        case HUFFMAN_CANONICAL_ERR_NUMERICAL_FAULT: return "Numerical computation anomaly";
        default: return "Unknown module error code";
    }
}
