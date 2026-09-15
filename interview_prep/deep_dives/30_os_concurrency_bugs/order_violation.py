"""Order violation: assuming one thread runs before another."""
import threading


def broken() -> dict:
    state: dict[str, int | None] = {"value": None}
    flag = threading.Event()

    def producer() -> None:
        state["value"] = 42
        flag.set()

    def consumer() -> dict:
        flag.wait()
        return state

    threads = [threading.Thread(target=producer), threading.Thread(target=consumer)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return state


if __name__ == "__main__":
    # An Event enforces the ordering; without it the consumer could read None.
    assert broken()["value"] == 42
    print("order violation avoided with Event")
