"""
Green's Function for Laplace/Poisson Equation on the Unit Disk with Dirichlet BC.
Reference: Hassani, Mathematical Methods for Physics, Ch. 21.
"""
import numpy as np

def greens_function_unit_disk(x: float, y: float, x0: float, y0: float) -> float:
    """
    G(r, r0) = (1 / 2 pi) ln( |r - r0| / ( |r0| |r - r0^*| ) ),
    where r0^* = r0 / |r0|^2 is the Kelvin inverted image point.
    """
    r_sq = x**2 + y**2
    r0_sq = x0**2 + y0**2
    r0_mag = np.sqrt(r0_sq)
    
    if np.isclose(r0_mag, 0.0):
        # Image is at infinity: G(r, 0) = (1 / 2 pi) ln(r)
        dist = np.sqrt(r_sq)
        return float((1.0 / (2.0 * np.pi)) * np.log(dist))
        
    dist_direct = np.sqrt((x - x0)**2 + (y - y0)**2)
    x_star = x0 / r0_sq
    y_star = y0 / r0_sq
    dist_image = np.sqrt((x - x_star)**2 + (y - y_star)**2)
    
    val = (1.0 / (2.0 * np.pi)) * np.log(dist_direct / (r0_mag * dist_image))
    return float(val)
