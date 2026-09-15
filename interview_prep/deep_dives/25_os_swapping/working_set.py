"""Working-set estimate and thrashing detection."""
from collections import deque
from dataclasses import dataclass, field


@dataclass
class WorkingSetModel:
    window: int
    references: deque[int] = field(default_factory=deque)

    def reference(self, page: int) -> int:
        self.references.append(page)
        if len(self.references) > self.window:
            self.references.popleft()
        return len(set(self.references))

    def thrashing(self, total_frames: int) -> bool:
        active = sum(1 for p in self.references)  # simplified: recent distinct pages
        return len(set(self.references)) > total_frames and active > total_frames


if __name__ == "__main__":
    model = WorkingSetModel(window=5)
    for page in [1, 2, 3, 1, 2, 4, 4, 4]:
        size = model.reference(page)
    assert size <= 5
    assert not model.thrashing(total_frames=3)
    print("working set size:", size)
