"""Mo's algorithm for offline range-sum queries."""
import math


def mo_queries(values: list[int], queries: list[tuple[int, int]]) -> list[int]:
    block = max(1, int(math.isqrt(len(values))))
    order = sorted(range(len(queries)), key=lambda i: (queries[i][0] // block, queries[i][1]))
    answers = [0] * len(queries)
    current_l, current_r, current_sum = 0, -1, 0
    for index in order:
        left, right = queries[index]
        while current_l > left:
            current_l -= 1
            current_sum += values[current_l]
        while current_r < right:
            current_r += 1
            current_sum += values[current_r]
        while current_l < left:
            current_sum -= values[current_l]
            current_l += 1
        while current_r > right:
            current_sum -= values[current_r]
            current_r -= 1
        answers[index] = current_sum
    return answers


if __name__ == "__main__":
    values = [1, 2, 3, 4, 5, 6, 7, 8]
    queries = [(0, 3), (2, 5), (1, 7)]
    assert mo_queries(values, queries) == [10, 18, 35]
    print("mo algorithm ok")
