#include <stdio.h>
#include <assert.h>
#include <stdlib.h>
#include "huffman_coding.h"

int main(void) {
    char data[] = {'a', 'b', 'c', 'd'};
    unsigned freq[] = {5, 9, 12, 13};
    HuffmanNode *root = build_huffman_tree(data, freq, 4);
    assert(root != NULL);
    assert(root->freq == 5 + 9 + 12 + 13);
    printf("test_huffman_coding PASSED\n");
    return 0;
}
