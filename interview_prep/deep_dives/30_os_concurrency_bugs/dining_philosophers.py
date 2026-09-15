"""Dining philosophers solved by breaking the circular wait."""
import threading


def run_philosophers(count: int = 5, meals: int = 20) -> list[int]:
    forks = [threading.Lock() for _ in range(count)]
    eaten = [0] * count

    def philosopher(index: int) -> None:
        left = index
        right = (index + 1) % count
        first, second = sorted((left, right))  # global order breaks the cycle
        for _ in range(meals):
            with forks[first]:
                with forks[second]:
                    eaten[index] += 1

    threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(count)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return eaten


if __name__ == "__main__":
    eaten = run_philosophers()
    assert all(count == 20 for count in eaten)
    print("philosophers ok:", eaten)
