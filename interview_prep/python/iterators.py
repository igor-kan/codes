"""Iterator protocol and itertools."""
import itertools


class Countdown:
    def __init__(self, start: int) -> None:
        self.current = start

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1


if __name__ == "__main__":
    assert list(Countdown(3)) == [3, 2, 1]
    assert list(itertools.accumulate([1, 2, 3, 4])) == [1, 3, 6, 10]
    assert list(itertools.chain([1, 2], [3])) == [1, 2, 3]
    assert list(itertools.groupby("aabbbc")) != []
    print("ok")
