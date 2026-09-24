"""WKB Connection Formulas across Classical Turning Points via Airy Functions."""
import numpy as np
from scipy.special import airy


def wkb_airy_turning_point_matching(x: np.ndarray) -> tuple:
    """Evaluate Airy functions Ai(x) and Bi(x) describing smooth connection across turning point."""
    ai, aip, bi, bip = airy(x)
    return ai, bi
