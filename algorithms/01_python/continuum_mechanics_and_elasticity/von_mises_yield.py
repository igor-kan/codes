"""Von Mises and Tresca Plastic Yield Criteria.

Von Mises equivalent stress: sigma_vm = sqrt(3 * J2)
Yield condition: sigma_vm >= sigma_yield.
Tresca maximum shear stress: tau_max = 0.5 * (sigma_1 - sigma_3) >= 0.5 * sigma_yield.
"""
import numpy as np
from cauchy_stress_invariants import deviatoric_stress, principal_stresses


def von_mises_stress(sigma: np.ndarray) -> float:
    """Calculate von Mises equivalent stress sigma_vm = sqrt(3 * J2)."""
    _, J2, _ = deviatoric_stress(sigma)
    return float(np.sqrt(3.0 * J2))


def check_yield(sigma: np.ndarray, yield_strength: float) -> dict:
    """Check von Mises and Tresca yield criteria."""
    vm = von_mises_stress(sigma)
    s1, _, s3 = principal_stresses(sigma)
    tresca = s1 - s3
    
    return {
        "von_mises_stress": vm,
        "tresca_stress": tresca,
        "yield_strength": yield_strength,
        "von_mises_yielded": bool(vm >= yield_strength),
        "tresca_yielded": bool(tresca >= yield_strength),
        "safety_factor_vm": float(yield_strength / vm) if vm > 0 else np.inf
    }
