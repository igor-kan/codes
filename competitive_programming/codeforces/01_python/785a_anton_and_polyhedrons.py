"""Codeforces 785A - Anton and Polyhedrons."""
FACES = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20,
}


def anton_and_polyhedrons(names):
    return sum(FACES[name] for name in names)


if __name__ == "__main__":
    assert anton_and_polyhedrons(["Icosahedron", "Cube", "Tetrahedron"]) == 30
    print("785A anton and polyhedrons ok")
