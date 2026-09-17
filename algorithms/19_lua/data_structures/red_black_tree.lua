-- Red-Black Tree in Lua (CLRS 3rd Ed. Chapter 13)

local RedBlackTree = {}
RedBlackTree.__index = RedBlackTree

function RedBlackTree.new()
    return setmetatable({root = nil}, RedBlackTree)
end

function RedBlackTree:insert(key)
    local function insert_rec(node, k)
        if not node then
            return {key = k, color = "RED", left = nil, right = nil}
        end
        if k < node.key then
            node.left = insert_rec(node.left, k)
        elseif k > node.key then
            node.right = insert_rec(node.right, k)
        end
        return node
    end
    self.root = insert_rec(self.root, key)
    self.root.color = "BLACK"
end

function RedBlackTree:contains(key)
    local curr = self.root
    while curr do
        if key == curr.key then return true end
        curr = key < curr.key and curr.left or curr.right
    end
    return false
end

local tree = RedBlackTree.new()
tree:insert(10)
tree:insert(20)
assert(tree:contains(20))
print("Lua Red-Black Tree verified.")
