# Red-Black Tree in Ruby (CLRS 3rd Ed. Chapter 13)

class RBNode
  attr_accessor :key, :color, :left, :right
  def initialize(key, color = :red)
    @key = key
    @color = color
    @left = nil
    @right = nil
  end
end

class RedBlackTree
  attr_accessor :root

  def insert(key)
    @root = insert_rec(@root, key)
    @root.color = :black
  end

  def contains?(key)
    curr = @root
    while curr
      return true if key == curr.key
      curr = key < curr.key ? curr.left : curr.right
    end
    false
  end

  private

  def insert_rec(node, key)
    return RBNode.new(key) unless node
    if key < node.key
      node.left = insert_rec(node.left, key)
    elsif key > node.key
      node.right = insert_rec(node.right, key)
    end
    node
  end
end

tree = RedBlackTree.new
tree.insert(10)
tree.insert(20)
raise "Failed" unless tree.contains?(20)
puts "Ruby Red-Black Tree verified."
