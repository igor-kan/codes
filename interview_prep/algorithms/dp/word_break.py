def word_break(s: str, words: list[str]) -> bool:
    wordset = set(words)
    dp = [False] * (len(s) + 1)
    dp[0] = True
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordset:
                dp[i] = True
                break
    return dp[-1]


if __name__ == "__main__":
    assert word_break("leetcode", ["leet", "code"])
    assert not word_break("catsandog", ["cats", "dog", "sand", "and", "cat"])
    print("ok")
