#include "huffman_coding.h"
#include <stdlib.h>

static HuffmanNode* create_node(char data, unsigned freq) {
    HuffmanNode *node = (HuffmanNode *)malloc(sizeof(HuffmanNode));
    node->data = data;
    node->freq = freq;
    node->left = node->right = NULL;
    return node;
}

HuffmanNode* build_huffman_tree(const char *data, const unsigned *freq, int size) {
    if (size <= 0) return NULL;
    HuffmanNode **nodes = (HuffmanNode **)malloc(size * sizeof(HuffmanNode *));
    for (int i = 0; i < size; ++i) {
        nodes[i] = create_node(data[i], freq[i]);
    }
    int cur_size = size;
    while (cur_size > 1) {
        // Find two smallest nodes
        int min1 = 0, min2 = 1;
        if (nodes[min2]->freq < nodes[min1]->freq) {
            min1 = 1; min2 = 0;
        }
        for (int i = 2; i < cur_size; ++i) {
            if (nodes[i]->freq < nodes[min1]->freq) {
                min2 = min1;
                min1 = i;
            } else if (nodes[i]->freq < nodes[min2]->freq) {
                min2 = i;
            }
        }
        HuffmanNode *parent = create_node('$', nodes[min1]->freq + nodes[min2]->freq);
        parent->left = nodes[min1];
        parent->right = nodes[min2];
        
        int first = (min1 > min2) ? min1 : min2;
        int second = (min1 < min2) ? min1 : min2;
        nodes[second] = parent;
        nodes[first] = nodes[cur_size - 1];
        cur_size--;
    }
    HuffmanNode *root = nodes[0];
    free(nodes);
    return root;
}
