"""Acousto-Optic Modulator (AOM) Bragg Diffraction.

Bragg condition: sin(theta_B) = lambda * f_acoustic / (2 * v_sound).
Diffraction efficiency in Bragg regime: eta = sin^2(pi * L / (2 * lambda) * sqrt(2 * M2 * I_a)).
"""
import numpy as np


def aom_bragg_angle(optical_wavelength: float, acoustic_freq: float, sound_speed: float) -> float:
    """Calculate internal Bragg angle in radians."""
    sin_theta_B = optical_wavelength * acoustic_freq / (2.0 * sound_speed)
    if sin_theta_B > 1.0:
        raise ValueError("Wavelength and frequency exceed physical Bragg diffraction limit")
    return float(np.arcsin(sin_theta_B))


def aom_diffraction_efficiency(L_interaction: float, optical_wavelength: float,
                               acoustic_power_density: float, M2_figure_of_merit: float = 1e-15) -> float:
    """Calculate 1st-order Bragg diffraction efficiency eta."""
    phi = (np.pi * L_interaction / optical_wavelength) * np.sqrt(0.5 * M2_figure_of_merit * acoustic_power_density)
    return float(np.sin(phi)**2)
