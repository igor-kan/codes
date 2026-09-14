"""Dining philosophers with ordered lock acquisition to avoid deadlock."""
import threading


def run_philosophers(count: int = 5, meals_each: int = 20) -> None:
    forks = [threading.Lock() for _ in range(count)]
    eaten = [0] * count

    def philosopher(index: int) -> None:
        left, right = index, (index + 1) % count
        first, second = sorted((left, right))  # global ordering prevents deadlock
        for _ in range(meals_each):
            with forks[first]:
                with forks[second]:
                    eaten[index] += 1

    threads = [threading.Thread(target=philosopher, args=(i,)) for i in range(count)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    assert all(count == meals_each for count in eaten)


if __name__ == "__main__":
    run_philosophers()
    print("philosophers ok")
