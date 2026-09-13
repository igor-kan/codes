/**
 * Huffman Encoding and Decoding Algorithm in C++.
 */

#include <iostream>
#include <string>
#include <queue>
#include <unordered_map>
#include <vector>
#include <cassert>

struct HuffmanNode {
    char ch;
    int freq;
    HuffmanNode* left;
    HuffmanNode* right;

    HuffmanNode(char c, int f, HuffmanNode* l = nullptr, HuffmanNode* r = nullptr)
        : ch(c), freq(f), left(l), right(r) {}
};

struct Compare {
    bool operator()(HuffmanNode* l, HuffmanNode* r) {
        return l->freq > r->freq;
    }
};

void generate_codes(HuffmanNode* root, const std::string& str, std::unordered_map<char, std::string>& huffmanCode) {
    if (!root) return;
    if (!root->left && !root->right) {
        huffmanCode[root->ch] = str;
    }
    generate_codes(root->left, str + "0", huffmanCode);
    generate_codes(root->right, str + "1", huffmanCode);
}

HuffmanNode* build_tree(const std::string& text) {
    std::unordered_map<char, int> freq;
    for (char ch : text) freq[ch]++;

    std::priority_queue<HuffmanNode*, std::vector<HuffmanNode*>, Compare> pq;
    for (auto pair : freq) {
        pq.push(new HuffmanNode(pair.first, pair.second));
    }

    while (pq.size() > 1) {
        HuffmanNode* left = pq.top(); pq.pop();
        HuffmanNode* right = pq.top(); pq.pop();
        int sum = left->freq + right->freq;
        pq.push(new HuffmanNode('\0', sum, left, right));
    }

    return pq.top();
}

std::string decode(HuffmanNode* root, const std::string& encoded) {
    std::string ans = "";
    HuffmanNode* curr = root;
    for (char bit : encoded) {
        if (bit == '0') curr = curr->left;
        else curr = curr->right;

        if (!curr->left && !curr->right) {
            ans += curr->ch;
            curr = root;
        }
    }
    return ans;
}

int main() {
    std::string text = "this is an example for a huffman encoding demonstration";
    HuffmanNode* root = build_tree(text);

    std::unordered_map<char, std::string> huffmanCode;
    generate_codes(root, "", huffmanCode);

    std::string encoded = "";
    for (char ch : text) encoded += huffmanCode[ch];

    std::string decoded = decode(root, encoded);
    assert(decoded == text);

    std::cout << "[C++ Huffman] Message decoded successfully: " << decoded.substr(0, 20) << "..." << std::endl;
    return 0;
}
