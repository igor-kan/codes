"""
Adaptive Runge-Kutta-Fehlberg (RK45) ODE Integrator and Disjoint Set Union (DSU).

Why Python for this module?
Python combines high-level mathematical readability with flexible function passing,
making it the lingua franca for prototyping numerical algorithms before lowering
to C/Fortran/Rust.
"""

import numpy as np
from typing import Callable, Tuple, List

def rk45_adaptive_step(f: Callable[[float, np.ndarray], np.ndarray],
                       t: float, y: np.ndarray, h: float,
                       tol: float = 1e-6) -> Tuple[float, np.ndarray, float, bool]:
    """
    Performs a single adaptive step using the Fehlberg 4(5) Butcher Tableau.
    Computes both 4th and 5th order approximations to estimate local truncation error.
    """
    k1 = h * f(t, y)
    k2 = h * f(t + (1/4)*h, y + (1/4)*k1)
    k3 = h * f(t + (3/8)*h, y + (3/32)*k1 + (9/32)*k2)
    k4 = h * f(t + (12/13)*h, y + (1932/2197)*k1 - (7200/2197)*k2 + (7296/2197)*k3)
    k5 = h * f(t + h, y + (439/216)*k1 - 8*k2 + (3680/513)*k3 - (845/4104)*k4)
    k6 = h * f(t + (1/2)*h, y - (8/27)*k1 + 2*k2 - (3544/2565)*k3 + (1859/4104)*k4 - (11/40)*k5)
    
    # 4th-order estimate
    y4 = y + (25/216)*k1 + (1408/2565)*k3 + (2197/4104)*k4 - (1/5)*k5
    # 5th-order estimate
    y5 = y + (16/135)*k1 + (6656/12825)*k3 + (28561/56430)*k4 - (9/50)*k5 + (2/55)*k6
    
    error = np.linalg.norm(y5 - y4, ord=np.inf)
    
    # Step size adaptation factor with safety margin 0.84
    if error > 0:
        s = 0.84 * (tol / error) ** 0.2
        s = max(0.1, min(s, 4.0)) # clamp step adjustment
    else:
        s = 4.0
        
    if error <= tol:
        return t + h, y5, h * s, True
    else:
        return t, y, h * s, False

class DisjointSetUnion:
    """Disjoint Set Union (DSU) with union-by-rank and recursive path compression."""
    def __init__(self, size: int):
        self.parent = list(range(size))
        self.rank = [0] * size
        self.num_components = size
        
    def find(self, i: int) -> int:
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i]) # Path compression
        return self.parent[i]
        
    def union(self, i: int, j: int) -> bool:
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i == root_j:
            return False
            
        # Union by rank
        if self.rank[root_i] < self.rank[root_j]:
            self.parent[root_i] = root_j
        elif self.rank[root_i] > self.rank[root_j]:
            self.parent[root_j] = root_i
        else:
            self.parent[root_j] = root_i
            self.rank[root_i] += 1
            
        self.num_components -= 1
        return True

if __name__ == "__main__":
    print("Python Module: Testing RK45 and DSU")
    # Test harmonic oscillator: y" + y = 0 -> y0' = y1, y1' = -y0
    f = lambda t, y: np.array([y[1], -y[0]])
    t, y, h = 0.0, np.array([1.0, 0.0]), 0.1
    t_next, y_next, h_next, ok = rk45_adaptive_step(f, t, y, h)
    print(f"RK45 Step: t={t_next:.3f}, y={y_next}, accepted={ok}")
    
    dsu = DisjointSetUnion(5)
    dsu.union(0, 1)
    dsu.union(1, 2)
    assert dsu.find(0) == dsu.find(2)
    print("DSU verification successful: elements 0 and 2 belong to the same component.")
