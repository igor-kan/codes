"""Gutenberg-Richter Frequency-Magnitude Distribution and b-value estimation."""

from typing import Sequence
import numpy as np


class GutenbergRichterLaw:
    """log10(N) = a - b * M."""

    @classmethod
    def cumulative_count(cls, a_value: float, b_value: float, magnitude: float) -> float:
        """N(>= M) = 10^(a - b * M)."""
        return float(10.0 ** (a_value - b_value * magnitude))

    @classmethod
    def estimate_b_value_aki_utsu(
        cls, magnitudes: Sequence[float], m_cutoff: float, bin_width: float = 0.1
    ) -> float:
        """Aki-Utsu Maximum Likelihood Estimator:
        b = log10(e) / ( mean(M) - (M_cutoff - bin_width / 2) ).
        """
        m_valid = np.array([m for m in magnitudes if m >= m_cutoff])
        if len(m_valid) == 0:
            raise ValueError("No events above cutoff magnitude.")
        mean_m = np.mean(m_valid)
        denom = mean_m - (m_cutoff - 0.5 * bin_width)
        return float(np.log10(np.e) / denom)
