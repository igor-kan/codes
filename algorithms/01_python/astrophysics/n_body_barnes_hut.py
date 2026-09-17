"""Hierarchical Barnes-Hut Tree for N-Body gravitational simulations."""

from typing import List, Optional
import numpy as np


class QuadTreeNode:
    """2D QuadTree node for Barnes-Hut force evaluation."""

    def __init__(self, x_min: float, x_max: float, y_min: float, y_max: float):
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = y_min
        self.y_max = y_max
        self.size = max(x_max - x_min, y_max - y_min)

        self.mass = 0.0
        self.com = np.zeros(2)
        self.is_leaf = True
        self.children: Optional[List[QuadTreeNode]] = None
        self.point: Optional[np.ndarray] = None
        self.point_mass: float = 0.0

    def insert(self, pos: np.ndarray, mass: float):
        if self.mass == 0.0:
            self.point = pos.copy()
            self.point_mass = mass
            self.mass = mass
            self.com = pos.copy()
            return

        if self.is_leaf:
            self.subdivide()
            old_pos = self.point
            old_mass = self.point_mass
            self.point = None
            self._insert_child(old_pos, old_mass)

        self._insert_child(pos, mass)
        # Update center of mass
        total_m = self.mass + mass
        self.com = (self.com * self.mass + pos * mass) / total_m
        self.mass = total_m

    def subdivide(self):
        mid_x = 0.5 * (self.x_min + self.x_max)
        mid_y = 0.5 * (self.y_min + self.y_max)
        self.children = [
            QuadTreeNode(self.x_min, mid_x, self.y_min, mid_y),
            QuadTreeNode(mid_x, self.x_max, self.y_min, mid_y),
            QuadTreeNode(self.x_min, mid_x, mid_y, self.y_max),
            QuadTreeNode(mid_x, self.x_max, mid_y, self.y_max),
        ]
        self.is_leaf = False

    def _insert_child(self, pos: np.ndarray, mass: float):
        mid_x = 0.5 * (self.x_min + self.x_max)
        mid_y = 0.5 * (self.y_min + self.y_max)
        idx = (1 if pos[0] >= mid_x else 0) + (2 if pos[1] >= mid_y else 0)
        self.children[idx].insert(pos, mass)

    def compute_force(self, pos: np.ndarray, theta: float = 0.5, g_const: float = 1.0, eps: float = 1e-4) -> np.ndarray:
        if self.mass == 0.0:
            return np.zeros(2)

        dr = self.com - pos
        dist = np.linalg.norm(dr)
        if dist < 1e-12:
            return np.zeros(2)

        if self.is_leaf or (self.size / dist < theta):
            f_mag = g_const * self.mass / (dist**2 + eps**2)
            return f_mag * (dr / dist)

        force = np.zeros(2)
        if self.children is not None:
            for child in self.children:
                force += child.compute_force(pos, theta, g_const, eps)
        return force
