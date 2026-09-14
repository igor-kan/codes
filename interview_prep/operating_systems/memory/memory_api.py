"""Memory API concepts: stack, heap and mmap."""
import ctypes
import mmap
import os


def heap_allocation() -> int:
    buffer = bytearray(1024)
    buffer[0] = 42
    return buffer[0]


def mmap_allocation(size: int = 4096) -> bytes:
    with mmap.mmap(-1, size) as region:
        region[0:6] = b"hello\n"
        return bytes(region[0:6])


def stack_address() -> int:
    local = 0
    return id(local)


if __name__ == "__main__":
    assert heap_allocation() == 42
    assert mmap_allocation() == b"hello\n"
    assert isinstance(stack_address(), int)
    print("memory api ok")
