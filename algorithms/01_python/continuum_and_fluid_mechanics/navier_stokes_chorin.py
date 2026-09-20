"""
Chorin's Projection Method for 2D Incompressible Navier-Stokes Equations.
References: Landau & Lifshitz - Fluid Mechanics (Vol. 6, Ch. 2).
"""
import numpy as np

class IncompressibleNavierStokes2D:
    def __init__(self, nx: int, ny: int, lx: float = 1.0, ly: float = 1.0, nu: float = 0.01):
        self.nx = nx
        self.ny = ny
        self.dx = lx / (nx - 1)
        self.dy = ly / (ny - 1)
        self.nu = nu

    def solve_pressure_poisson(self, div_u, p, n_iter=30):
        """Jacobi relaxation solver for pressure Poisson equation: div(grad p) = div(u*) / dt."""
        dx, dy = self.dx, self.dy
        for _ in range(n_iter):
            p_new = p.copy()
            p_new[1:-1, 1:-1] = (
                (dy**2 * (p[2:, 1:-1] + p[:-2, 1:-1]) +
                 dx**2 * (p[1:-1, 2:] + p[1:-1, :-2]) -
                 dx**2 * dy**2 * div_u[1:-1, 1:-1]) /
                (2.0 * (dx**2 + dy**2))
            )
            # Neumann boundary conditions: dp/dn = 0
            p_new[0, :] = p_new[1, :]
            p_new[-1, :] = p_new[-2, :]
            p_new[:, 0] = p_new[:, 1]
            p_new[:, -1] = p_new[:, -2]
            p = p_new
        return p

    def step(self, u, v, p, dt):
        """Predictor-corrector step."""
        dx, dy = self.dx, self.dy
        # Tentative velocity u*, v* (advection + diffusion)
        lap_u = (u[2:, 1:-1] - 2*u[1:-1, 1:-1] + u[:-2, 1:-1]) / dx**2 + (u[1:-1, 2:] - 2*u[1:-1, 1:-1] + u[1:-1, :-2]) / dy**2
        lap_v = (v[2:, 1:-1] - 2*v[1:-1, 1:-1] + v[:-2, 1:-1]) / dx**2 + (v[1:-1, 2:] - 2*v[1:-1, 1:-1] + v[1:-1, :-2]) / dy**2
        
        u_star = u.copy()
        v_star = v.copy()
        u_star[1:-1, 1:-1] += dt * self.nu * lap_u
        v_star[1:-1, 1:-1] += dt * self.nu * lap_v

        # Divergence of tentative velocity
        div_star = np.zeros_like(p)
        div_star[1:-1, 1:-1] = (
            (u_star[2:, 1:-1] - u_star[:-2, 1:-1]) / (2.0 * dx) +
            (v_star[1:-1, 2:] - v_star[1:-1, :-2]) / (2.0 * dy)
        ) / dt

        # Solve pressure Poisson equation
        p_new = self.solve_pressure_poisson(div_star, p)

        # Projection velocity update: u^{n+1} = u* - dt grad(p)
        u_new = u_star.copy()
        v_new = v_star.copy()
        u_new[1:-1, 1:-1] -= dt * (p_new[2:, 1:-1] - p_new[:-2, 1:-1]) / (2.0 * dx)
        v_new[1:-1, 1:-1] -= dt * (p_new[1:-1, 2:] - p_new[1:-1, :-2]) / (2.0 * dy)

        return u_new, v_new, p_new
