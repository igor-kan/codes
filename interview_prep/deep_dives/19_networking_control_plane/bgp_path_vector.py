"""BGP path-vector selection with simple policy preferences."""
from dataclasses import dataclass


@dataclass(frozen=True)
class Announcement:
    prefix: str
    as_path: tuple[int, ...]
    local_pref: int = 100
    origin: int = 0


def select_best(routes: list[Announcement]) -> Announcement:
    """Simplified BGP decision: highest local pref, then shortest AS path."""
    return min(routes, key=lambda r: (-r.local_pref, len(r.as_path), r.as_path, r.origin))


def detect_loop(route: Announcement, local_as: int) -> bool:
    return local_as in route.as_path


if __name__ == "__main__":
    routes = [
        Announcement("203.0.113.0/24", (64500, 64501,)),          # 2 hops
        Announcement("203.0.113.0/24", (64500, 64510, 64520)),    # 3 hops
        Announcement("203.0.113.0/24", (64500, 64530), local_pref=200),  # preferred
    ]
    best = select_best(routes)
    assert best.local_pref == 200 and best.as_path == (64500, 64530)
    assert detect_loop(Announcement("x", (65001, 65002)), local_as=65001)
    print("bgp selection ok")
