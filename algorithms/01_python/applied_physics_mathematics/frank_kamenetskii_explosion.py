"""
Frank-Kamenetskii Thermal Explosion Theory.
Reference: Zeldovich, Higher Mathematics for Beginners; Barenblatt.
"""
import numpy as np

def frank_kamenetskii_critical_parameter(geometry: str = "slab") -> float:
    """
    Critical value delta_cr of the Frank-Kamenetskii parameter delta = (Q E r_0^2 / (lambda R T_0^2)) k(T_0):
    - Infinite flat slab: delta_cr = 0.878
    - Infinite cylinder: delta_cr = 2.000
    - Sphere: delta_cr = 3.322
    If delta > delta_cr, thermal explosion occurs.
    """
    table = {
        "slab": 0.878457,
        "cylinder": 2.000000,
        "sphere": 3.32199
    }
    return table.get(geometry.lower(), 0.878457)

def will_explode(delta: float, geometry: str = "slab") -> bool:
    return delta > frank_kamenetskii_critical_parameter(geometry)
