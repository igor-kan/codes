"""Eertree (palindromic tree) counting distinct palindromes."""
class PalindromicTree:
    def __init__(self) -> None:
        self.length = [-1, 0]
        self.suffix_link = [0, 0]
        self.transitions: list[dict[str, int]] = [{}, {}]
        self.last = 1

    def add(self, text: str, index: int) -> bool:
        current = self.last
        while True:
            current_length = self.length[current]
            if index - 1 - current_length >= 0 and text[index - 1 - current_length] == text[index]:
                break
            current = self.suffix_link[current]
        if text[index] in self.transitions[current]:
            self.last = self.transitions[current][text[index]]
            return False
        node = len(self.length)
        self.length.append(self.length[current] + 2)
        self.transitions.append({})
        self.suffix_link.append(0)
        self.transitions[current][text[index]] = node
        if self.length[node] == 1:
            self.suffix_link[node] = 1
        else:
            temp = self.suffix_link[current]
            while True:
                temp_length = self.length[temp]
                if index - 1 - temp_length >= 0 and text[index - 1 - temp_length] == text[index]:
                    break
                temp = self.suffix_link[temp]
            self.suffix_link[node] = self.transitions[temp][text[index]]
        self.last = node
        return True


def count_distinct_palindromes(text: str) -> int:
    tree = PalindromicTree()
    distinct = 0
    for i, ch in enumerate(text):
        if tree.add(text, i):
            distinct += 1
    return distinct


if __name__ == "__main__":
    assert count_distinct_palindromes("abaaa") == 5
    print("palindromic tree ok")
