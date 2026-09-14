"""Lazy pipelines with generator functions."""
from itertools import islice


def read_lines(text: str):
    for line in text.splitlines():
        yield line.strip()


def non_empty(lines):
    for line in lines:
        if line:
            yield line


def numbers(lines):
    for line in lines:
        if line.isdigit():
            yield int(line)


if __name__ == "__main__":
    text = "1\n\n2\nfoo\n3\n"
    pipeline = numbers(non_empty(read_lines(text)))
    assert list(pipeline) == [1, 2, 3]

    def naturals():
        n = 0
        while True:
            yield n
            n += 1

    assert list(islice(naturals(), 5)) == [0, 1, 2, 3, 4]
    print("ok")
