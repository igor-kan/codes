"""Activity-selection problem (CLRS 16.1)."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Activity:
    start: int
    finish: int


def select_activities(activities: list[Activity]) -> list[Activity]:
    chosen: list[Activity] = []
    last_finish = float("-inf")
    for activity in sorted(activities, key=lambda a: a.finish):
        if activity.start >= last_finish:
            chosen.append(activity)
            last_finish = activity.finish
    return chosen


if __name__ == "__main__":
    acts = [Activity(1, 4), Activity(3, 5), Activity(0, 6),
            Activity(5, 7), Activity(3, 9), Activity(5, 9),
            Activity(6, 10), Activity(8, 11), Activity(8, 12),
            Activity(2, 14), Activity(12, 16)]
    chosen = select_activities(acts)
    assert [(a.start, a.finish) for a in chosen] == [(1, 4), (5, 7), (8, 11), (12, 16)]
    print("activity selection ok")
