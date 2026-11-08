/**
 * @file errors.cpp
 * @brief Rich diagnostic error reporting for Self-Balancing AVL Search Tree with Rotations.
 * Module: avl_balanced_tree
 */

typedef enum avl_balanced_tree_error {
    AVL_BALANCED_TREE_OK = 0,
    AVL_BALANCED_TREE_ERR_NULL = -100,
    AVL_BALANCED_TREE_ERR_CAPACITY = -101,
    AVL_BALANCED_TREE_ERR_CONVERGENCE = -102
} avl_balanced_tree_error_t;

const char* avl_balanced_tree_strerror(avl_balanced_tree_error_t err) {
    switch (err) {
        case AVL_BALANCED_TREE_OK: return "Success";
        case AVL_BALANCED_TREE_ERR_NULL: return "Encountered null pointer argument";
        case AVL_BALANCED_TREE_ERR_CAPACITY: return "Capacity limit exceeded";
        case AVL_BALANCED_TREE_ERR_CONVERGENCE: return "Numerical algorithm failed to converge";
        default: return "Unknown error";
    }
}
