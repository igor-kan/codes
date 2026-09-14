from collections import defaultdict


def group_anagrams(words: list[str]) -> list[list[str]]:
    buckets: dict[tuple, list[str]] = defaultdict(list)
    for word in words:
        buckets[tuple(sorted(word))].append(word)
    return list(buckets.values())


if __name__ == "__main__":
    result = group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    assert sorted(map(sorted, result)) == [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]]
    print("ok")
