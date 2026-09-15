// Self-balancing AVL tree.
class Node {
  constructor(key) {
    this.key = key;
    this.height = 1;
    this.left = null;
    this.right = null;
  }
}

const height = (node) => (node ? node.height : 0);
const update = (node) => {
  node.height = 1 + Math.max(height(node.left), height(node.right));
};

function rotateRight(y) {
  const x = y.left;
  y.left = x.right;
  x.right = y;
  update(y);
  update(x);
  return x;
}

function rotateLeft(x) {
  const y = x.right;
  x.right = y.left;
  y.left = x;
  update(x);
  update(y);
  return y;
}

function balance(node) {
  update(node);
  const factor = height(node.left) - height(node.right);
  if (factor > 1) {
    if (height(node.left.left) < height(node.left.right)) node.left = rotateLeft(node.left);
    return rotateRight(node);
  }
  if (factor < -1) {
    if (height(node.right.right) < height(node.right.left)) node.right = rotateRight(node.right);
    return rotateLeft(node);
  }
  return node;
}

function insert(node, key) {
  if (!node) return new Node(key);
  if (key < node.key) node.left = insert(node.left, key);
  else if (key > node.key) node.right = insert(node.right, key);
  else return node;
  return balance(node);
}

function inorder(node, out = []) {
  if (!node) return out;
  inorder(node.left, out);
  out.push(node.key);
  inorder(node.right, out);
  return out;
}

let root = null;
for (const key of [10, 20, 30, 40, 50, 25]) root = insert(root, key);
const out = inorder(root);
if (out.some((value, index) => index && out[index - 1] > value)) throw new Error("not sorted");
console.log("avl tree ok");
