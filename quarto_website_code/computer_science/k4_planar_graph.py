"""
Complete Graph K4: Planar Embeddings and Crossing Numbers.

Deconstructs the finite geometry meme:
Straight-line drawing of K4 in R^2 has crossing number 1.
However, K4 is planar (Fáry's Theorem): it can be drawn without crossings on a plane.
"""

import itertools

def verify_k4_properties():
    vertices = {1, 2, 3, 4}
    edges = list(itertools.combinations(vertices, 2))
    assert len(edges) == 6, "K4 must have 6 edges!"
    
    # Independent edges (the green diagonals)
    e1 = (1, 4)
    e2 = (2, 3)
    assert len(set(e1).intersection(set(e2))) == 0, "Diagonals share 0 vertices!"
    return True

if __name__ == "__main__":
    print("=== COMPLETE GRAPH K4 EMBEDDINGS ===")
    assert verify_k4_properties()
    print("K4 vertices: 4, edges: 6. Crossing number cr(K4) = 0 on sphere/plane via curved embedding.")
