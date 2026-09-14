"""Bucket sort for floats in [0, 1)."""


def bucket_sort(values: list[float], buckets: int = 10) -> list[float]:
    if not values:
        return []
    containers: list[list[float]] = [[] for _ in range(buckets)]
    for value in values:
        containers[min(int(value * buckets), buckets - 1)].append(value)
    return [v for bucket in containers for v in sorted(bucket)]


if __name__ == "__main__":
    data = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12]
    assert bucket_sort(data) == sorted(data)
    print(bucket_sort(data))
