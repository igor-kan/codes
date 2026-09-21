"""Acoustic vs. Relativistic Optical Doppler Effect.

Acoustic Doppler shift: f' = f * (c +- v_r) / (c -+ v_s).
Relativistic optical Doppler shift: f' = f * sqrt((1 - beta) / (1 + beta)) for receding source.
"""
import numpy as np


def acoustic_doppler_frequency(f_source: float, v_sound: float,
                               v_receiver: float, v_source: float) -> float:
    """Calculate received frequency with signed velocities (positive = moving towards each other)."""
    return float(f_source * (v_sound + v_receiver) / (v_sound - v_source))


def relativistic_optical_doppler(f_source: float, beta: float) -> float:
    """Relativistic Doppler shift for velocity v = beta * c (positive beta = receding)."""
    if abs(beta) >= 1.0:
        raise ValueError("|beta| must be < 1.0")
    return float(f_source * np.sqrt((1.0 - beta) / (1.0 + beta)))
