"""Hash-based collections and lookup patterns."""
from collections import Counter, defaultdict, ChainMap


def word_counts(text: str) -> Counter:
    return Counter(text.lower().split())


def invert(mapping: dict) -> dict:
    inverted: dict = defaultdict(list)
    for key, value in mapping.items():
        inverted[value].append(key)
    return dict(inverted)


if __name__ == "__main__":
    assert word_counts("the cat the hat").most_common(1) == [("the", 2)]
    assert invert({"a": 1, "b": 1, "c": 2}) == {1: ["a", "b"], 2: ["c"]}

    config = ChainMap({"debug": True}, {"debug": False, "port": 8080})
    assert config["debug"] is True and config["port"] == 8080
    print("ok")
