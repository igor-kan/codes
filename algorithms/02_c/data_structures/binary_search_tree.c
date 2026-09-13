#include <stdlib.h>
typedef struct BST { int key; struct BST *left, *right; } BST;
BST *insert(BST *root, int key){
    if(!root){ BST *n=malloc(sizeof(BST)); n->key=key; n->left=n->right=NULL; return n; }
    if(key<root->key) root->left=insert(root->left,key);
    else if(key>root->key) root->right=insert(root->right,key);
    return root;
}
BST *search(BST *root, int key){
    return !root||root->key==key?root:key<root->key?search(root->left,key):search(root->right,key);
}
