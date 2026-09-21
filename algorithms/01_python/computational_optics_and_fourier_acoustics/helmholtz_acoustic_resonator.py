"""Helmholtz Acoustic Resonator Resonance Frequency and End Corrections.

Resonance frequency: f_0 = (c / 2*pi) * sqrt(S / (V * L_eff)).
End-corrected neck length: L_eff = L + 0.85 * d (flanged) or L + 0.6 * d (unflanged).
"""
import numpy as np


def helmholtz_resonance_frequency(volume_V: float, neck_diameter: float, neck_length: float,
                                  sound_speed: float = 343.0, flanged: bool = True) -> float:
    """Calculate Helmholtz resonance frequency f_0 in Hz."""
    S = 0.25 * np.pi * neck_diameter**2
    end_correction = 0.85 * neck_diameter if flanged else 0.6 * neck_diameter
    L_eff = neck_length + end_correction
    return float((sound_speed / (2.0 * np.pi)) * np.sqrt(S / (volume_V * L_eff)))
