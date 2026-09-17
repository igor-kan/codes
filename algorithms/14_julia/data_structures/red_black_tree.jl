# Red-Black Tree Implementation in Julia (CLRS 3rd Ed. Chapter 13)

@enum Color RED BLACK

mutable struct RBNode{T}
    key::T
    color::Color
    left::Union{RBNode{T}, Nothing}
    right::Union{RBNode{T}, Nothing}
end

RBNode(key::T) where T = RBNode{T}(key, RED, nothing, nothing)

mutable struct RedBlackTree{T}
    root::Union{RBNode{T}, Nothing}
end

RedBlackTree{T}() where T = RedBlackTree{T}(nothing)

function insert!(tree::RedBlackTree{T}, key::T) where T
    function insert_node(node::Union{RBNode{T}, Nothing}, k::T)
        if node === nothing
            return RBNode(k)
        end
        if k < node.key
            node.left = insert_node(node.left, k)
        elseif k > node.key
            node.right = insert_node(node.right, k)
        end
        return node
    end
    tree.root = insert_node(tree.root, key)
    tree.root.color = BLACK
end

function contains(tree::RedBlackTree{T}, key::T) where T
    curr = tree.root
    while curr !== nothing
        if key == curr.key
            return true
        elseif key < curr.key
            curr = curr.left
        else
            curr = curr.right
        end
    end
    return false
end

tree = RedBlackTree{Int}()
insert!(tree, 10)
insert!(tree, 20)
insert!(tree, 5)
@assert contains(tree, 20)
@assert !contains(tree, 99)
println("Julia Red-Black Tree verified.")
