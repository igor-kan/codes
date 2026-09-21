#ifndef HUFFMAN_CODING_H
#define HUFFMAN_CODING_H

typedef struct HuffmanNode {
    char data;
    unsigned freq;
    struct HuffmanNode *left, *right;
} HuffmanNode;

HuffmanNode* build_huffman_tree(const char *data, const unsigned *freq, int size);

#endif
