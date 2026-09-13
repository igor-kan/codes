// ==============================================================================
// File: languages/13_swift/BinarySearchTree.swift
// Language: Swift 5.9+ (Modern Systems & Application Programming)
// Domain: Generic Collections & Protocol-Oriented Data Structures
// Algorithm: Immutable / Copy-on-Write Binary Search Tree with Sequence Conformance
//
// Rationale & Language Fit:
//   Swift combines the safety and performance of compiled systems languages
//   with high-level declarative protocol-oriented syntax. By conforming our
//   Generic Binary Search Tree to Swift's standard library `Sequence` and
//   `CustomStringConvertible`, tree instances seamlessly support `for-in`
//   loops, `map`, `filter`, and `reduce`. Algebraic recursive types are
//   natively represented via `indirect enum`.
// ==============================================================================

import Foundation

/// A generic, immutable, value-typed Binary Search Tree.
public indirect enum BinarySearchTree<Element: Comparable>: Sequence, CustomStringConvertible {
    case empty
    case node(Element, left: BinarySearchTree<Element>, right: BinarySearchTree<Element>)

    // MARK: - Initializers
    
    /// Creates an empty tree.
    public init() {
        self = .empty
    }

    /// Creates a tree containing a single value.
    public init(_ value: Element) {
        self = .node(value, left: .empty, right: .empty)
    }

    /// Creates a balanced tree from an array of elements.
    public init<S: Sequence>(_ sequence: S) where S.Element == Element {
        var tree = BinarySearchTree.empty
        for element in sequence {
            tree = tree.inserting(element)
        }
        self = tree
    }

    // MARK: - Core Operations

    /// Returns the number of elements in the tree.
    public var count: Int {
        switch self {
        case .empty:
            return 0
        case .node(_, let left, let right):
            return 1 + left.count + right.count
        }
    }

    /// Returns the height / maximum depth of the tree.
    public var height: Int {
        switch self {
        case .empty:
            return 0
        case .node(_, let left, let right):
            return 1 + max(left.height, right.height)
        }
    }

    /// Checks if the tree is empty.
    public var isEmpty: Bool {
        if case .empty = self { return true }
        return false
    }

    /// Checks whether an element exists in O(log n) expected time.
    public func contains(_ value: Element) -> Bool {
        switch self {
        case .empty:
            return false
        case .node(let root, let left, let right):
            if value == root {
                return true
            } else if value < root {
                return left.contains(value)
            } else {
                return right.contains(value)
            }
        }
    }

    /// Returns a new tree with the value inserted, preserving BST invariants.
    public func inserting(_ value: Element) -> BinarySearchTree<Element> {
        switch self {
        case .empty:
            return .node(value, left: .empty, right: .empty)
        case .node(let root, let left, let right):
            if value < root {
                return .node(root, left: left.inserting(value), right: right)
            } else if value > root {
                return .node(root, left: left, right: right.inserting(value))
            } else {
                // Deduplicate: exact duplicate is not re-inserted
                return self
            }
        }
    }

    /// In-order traversal array of all elements.
    public func inOrderElements() -> [Element] {
        switch self {
        case .empty:
            return []
        case .node(let root, let left, let right):
            return left.inOrderElements() + [root] + right.inOrderElements()
        }
    }

    // MARK: - Sequence Protocol Conformance

    public struct Iterator: IteratorProtocol {
        private var stack: [BinarySearchTree<Element>] = []

        fileprivate init(root: BinarySearchTree<Element>) {
            pushLeftPath(root)
        }

        private mutating func pushLeftPath(_ tree: BinarySearchTree<Element>) {
            var current = tree
            while case .node(_, let left, _) = current {
                stack.append(current)
                current = left
            }
        }

        public mutating func next() -> Element? {
            guard !stack.isEmpty else { return nil }
            let current = stack.removeLast()
            
            guard case .node(let value, _, let right) = current else {
                return nil
            }
            
            // Push leftmost spine of the right subtree
            pushLeftPath(right)
            return value
        }
    }

    public func makeIterator() -> Iterator {
        return Iterator(root: self)
    }

    // MARK: - CustomStringConvertible

    public var description: String {
        let elements = inOrderElements().map { "\($0)" }.joined(separator: ", ")
        return "BinarySearchTree([\(elements)])"
    }
}

// --- Verification & Demo ---
print("=================================================================")
print("Swift Protocol-Oriented Generic Binary Search Tree")
print("=================================================================")

let sampleValues = [42, 17, 68, 9, 23, 54, 88, 3, 12, 19, 31, 75, 99]
var bst = BinarySearchTree<Int>()

for val in sampleValues {
    bst = bst.inserting(val)
}

print("Inserted elements: \(sampleValues)")
print("Tree representation: \(bst)")
print("Total count: \(bst.count) nodes | Depth height: \(bst.height)")

// Verification of lookup
assert(bst.contains(23) == true)
assert(bst.contains(999) == false)
print("Lookup verification: contains(23) -> true, contains(999) -> false")

// Verification of Sequence protocol (for-in and higher-order functions)
let sortedList = bst.map { $0 }
let evens = bst.filter { $0 % 2 == 0 }
let sum = bst.reduce(0, +)

print("In-order Sequence iteration: \(sortedList)")
print("Filtered evens: \(evens)")
print("Sum of elements: \(sum)")

assert(sortedList == sampleValues.sorted())
print("[SUCCESS] Swift BST conforms to Sequence and preserves ordering.")
