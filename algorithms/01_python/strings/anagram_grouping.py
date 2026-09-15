"""Group anagrams using sorted keys and canonical counts."""
from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[str, list[str]] = defaultdict(list)
    for word in words:
        key = "".join(sorted(word))
        groups[key].append(word)
    return list(groups.values())


def is_anagram(a: str, b: str) -> bool:
    if len(a) != len(b):
        return False
    counts: dict[str, int] = defaultdict(int)
    for ch in a:
        counts[ch] += 1
    for ch in b:
        counts[ch] -= 1
        if counts[ch] < 0:
            return False
    return True


if __name__ == "__main__":
    assert is_anagram("listen", "silent")
    assert sorted(map(sorted, group_anagrams(["eat", "tea", "tan", "ate"]))) == [["ate", "eat", "tea"], ["tan"]]
    print("anagram grouping ok")
