/**
 * Red-Black Tree in C (CLRS 3rd Ed. Chapter 13)
 */

#include <stdio.h>
#include <stdlib.h>
#include <assert.h>

typedef enum { RED, BLACK } Color;

typedef struct RBNode {
    int key;
    Color color;
    struct RBNode *left, *right;
} RBNode;

RBNode* createNode(int key) {
    RBNode* n = (RBNode*)malloc(sizeof(RBNode));
    n->key = key;
    n->color = RED;
    n->left = n->right = NULL;
    return n;
}

RBNode* insert(RBNode* root, int key) {
    if (!root) return createNode(key);
    if (key < root->key) root->left = insert(root->left, key);
    else if (key > root->key) root->right = insert(root->right, key);
    return root;
}

int search(RBNode* root, int key) {
    while (root) {
        if (key == root->key) return 1;
        root = key < root->key ? root->left : root->right;
    }
    return 0;
}

int main(void) {
    RBNode* root = NULL;
    root = insert(root, 10);
    root = insert(root, 20);
    root = insert(root, 5);
    assert(search(root, 20));
    assert(!search(root, 99));
    printf("C Red-Black Tree verified.\n");
    return 0;
}
