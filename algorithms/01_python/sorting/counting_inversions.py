"""Count inversions with a modified merge sort (CLRS 2.4 style)."""


def count_inversions(values: list[int]) -> int:
    def sort_count(items: list[int]) -> tuple[list[int], int]:
        if len(items) <= 1:
            return items, 0
        mid = len(items) // 2
        left, inv_left = sort_count(items[:mid])
        right, inv_right = sort_count(items[mid:])
        merged: list[int] = []
        i = j = inversions = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                inversions += len(left) - i
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inv_left + inv_right + inversions

    return sort_count(values)[1]


if __name__ == "__main__":
    assert count_inversions([2, 4, 1, 3, 5]) == 3
    assert count_inversions([5, 4, 3, 2, 1]) == 10
    print("counting inversions ok")
