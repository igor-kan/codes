"""list vs array vs deque vs tuple."""
import array
import sys
from collections import deque


def types_demo() -> dict:
    return {
        "list": sys.getsizeof([0] * 1000),
        "array": sys.getsizeof(array.array("l", [0] * 1000)),
        "deque": sys.getsizeof(deque(range(1000))),
        "tuple": sys.getsizeof(tuple(range(1000))),
    }


if __name__ == "__main__":
    buffer = array.array("d", [1.0, 2.0, 3.0])
    assert buffer.tolist() == [1.0, 2.0, 3.0]
    queue = deque([1, 2, 3], maxlen=3)
    queue.appendleft(0)
    assert list(queue) == [0, 1, 2]
    print(types_demo())
