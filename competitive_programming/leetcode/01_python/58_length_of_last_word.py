"""LeetCode 58 - Length of Last Word."""
def length_of_last_word(text):
    words = text.split()
    return len(words[-1]) if words else 0


if __name__ == "__main__":
    assert length_of_last_word("Hello World") == 5
    assert length_of_last_word("   fly me   to   the moon  ") == 4
    print("58 length of last word ok")
