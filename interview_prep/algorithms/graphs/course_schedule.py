from collections import deque


def can_finish(num_courses: int, prerequisites: list[list[int]]) -> bool:
    graph: dict[int, list[int]] = {i: [] for i in range(num_courses)}
    indegree = [0] * num_courses
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    queue = deque(c for c in range(num_courses) if indegree[c] == 0)
    taken = 0
    while queue:
        node = queue.popleft()
        taken += 1
        for nxt in graph[node]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                queue.append(nxt)
    return taken == num_courses


if __name__ == "__main__":
    assert can_finish(2, [[1, 0]])
    assert not can_finish(2, [[1, 0], [0, 1]])
    print("ok")
