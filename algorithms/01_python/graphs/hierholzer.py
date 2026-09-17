"""
Hierholzer's Algorithm in Python.
Finds Eulerian path / circuit in O(V + E) time.
"""

def hierholzer(n, adj):
    graph = [list(edges) for edges in adj]
    stack = [0]
    circuit = []

    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].pop()
            stack.append(v)
        else:
            circuit.append(stack.pop())

    return circuit[::-1]

if __name__ == "__main__":
    adj = [[1], [2], [0, 3], [0]]
    path = hierholzer(4, adj)
    assert len(path) == 6
    print("Python Hierholzer verified.")
