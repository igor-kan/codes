"""Codeforces 158A - Next Round."""
def next_round(scores, k):
    threshold = scores[k - 1]
    return sum(1 for score in scores if score >= threshold and score > 0)


if __name__ == "__main__":
    assert next_round([10, 9, 8, 7, 7, 7, 5, 5], 5) == 6
    assert next_round([0, 0, 0, 0], 2) == 0
    print("158A next round ok")
