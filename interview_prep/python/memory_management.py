"""References, interning and weak references."""
import sys
import weakref


class Node:
    def __init__(self, name: str) -> None:
        self.name = name


if __name__ == "__main__":
    a = "hello"
    b = "hello"
    assert a is b  # short string interning

    x = [1, 2, 3]
    y = x
    assert x is y and sys.getrefcount(x) >= 2

    node = Node("root")
    ref = weakref.ref(node)
    assert ref() is node
    del node
    assert ref() is None
    print("ok")
