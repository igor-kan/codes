package data_structures
type TrieNode struct { children [26]*TrieNode; end bool }
type Trie struct { root *TrieNode }
func NewTrie() *Trie { return &Trie{&TrieNode{}} }
func (t *Trie) Insert(w string) {
	n:=t.root; for _,c:=range w { i:=c-97; if n.children[i]==nil { n.children[i]=&TrieNode{} }; n=n.children[i] }; n.end=true
}
func (t *Trie) Search(w string) bool {
	n:=t.root; for _,c:=range w { i:=c-97; if n.children[i]==nil { return false }; n=n.children[i] }; return n.end
}