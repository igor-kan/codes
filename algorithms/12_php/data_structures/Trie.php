<?php
declare(strict_types=1);

namespace Algorithms\DataStructures;

class Trie {
    private array $root;
    private bool $isEnd;

    public function __construct(bool $isEnd = false) {
        $this->root = [];
        $this->isEnd = $isEnd;
    }

    public function insert(string $word): void {
        $node = $this;
        for ($i = 0; $i < strlen($word); $i++) {
            $c = $word[$i];
            if (!isset($node->root[$c])) {
                $node->root[$c] = new Trie();
            }
            $node = $node->root[$c];
        }
        $node->isEnd = true;
    }

    public function search(string $word): bool {
        $node = $this;
        for ($i = 0; $i < strlen($word); $i++) {
            $c = $word[$i];
            if (!isset($node->root[$c])) {
                return false;
            }
            $node = $node->root[$c];
        }
        return $node->isEnd;
    }

    public function startsWith(string $prefix): bool {
        $node = $this;
        for ($i = 0; $i < strlen($prefix); $i++) {
            $c = $prefix[$i];
            if (!isset($node->root[$c])) {
                return false;
            }
            $node = $node->root[$c];
        }
        return true;
    }
}

if (php_sapi_name() === 'cli' && basename($_SERVER['SCRIPT_FILENAME'] ?? '') === basename(__FILE__)) {
    echo "[PHP Trie] Testing Trie data structure\n";
    $trie = new Trie();
    $trie->insert("apple");
    echo "search apple: " . ($trie->search("apple") ? 'true' : 'false') . " (expected true)\n";
    echo "search app: " . ($trie->search("app") ? 'true' : 'false') . " (expected false)\n";
    echo "startsWith app: " . ($trie->startsWith("app") ? 'true' : 'false') . " (expected true)\n";
    $trie->insert("app");
    echo "search app: " . ($trie->search("app") ? 'true' : 'false') . " (expected true)\n";
    echo "[PHP Trie] Test completed.\n";
}