using System.Collections.Generic;

namespace Algorithms.DataStructures
{
    public class TrieNode
    {
        public Dictionary<char, TrieNode> Children { get; } = new();
        public bool IsEndOfWord { get; set; }
    }

    public class Trie
    {
        private readonly TrieNode _root = new();

        public void Insert(string word)
        {
            var current = _root;
            foreach (char ch in word)
            {
                if (!current.Children.TryGetValue(ch, out var next))
                {
                    next = new TrieNode();
                    current.Children[ch] = next;
                }
                current = next;
            }
            current.IsEndOfWord = true;
        }

        public bool Search(string word)
        {
            var current = _root;
            foreach (char ch in word)
            {
                if (!current.Children.TryGetValue(ch, out var next))
                    return false;
                current = next;
            }
            return current.IsEndOfWord;
        }

        public bool StartsWith(string prefix)
        {
            var current = _root;
            foreach (char ch in prefix)
            {
                if (!current.Children.TryGetValue(ch, out var next))
                    return false;
                current = next;
            }
            return true;
        }
    }
}
