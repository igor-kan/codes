"""Modified Omori Law for aftershock frequency decay."""

import numpy as np


class OmoriLaw:
    """Rate of aftershocks following mainshock:
    n(t) = K / (t + c)^p
    where typically p is close to 1.0.
    """

    @classmethod
    def rate(cls, t_days: float, k: float, c_days: float, p: float = 1.0) -> float:
        """Instantaneous aftershock rate at time t days."""
        return float(k / ((t_days + c_days) ** p))

    @classmethod
    def cumulative_events(cls, t_start: float, t_end: float, k: float, c_days: float, p: float = 1.0) -> float:
        """Integral of rate from t_start to t_end."""
        if p == 1.0:
            return float(k * (np.log(t_end + c_days) - np.log(t_start + c_days)))
        else:
            term1 = (t_end + c_days) ** (1.0 - p)
            term2 = (t_start + c_days) ** (1.0 - p)
            return float((k / (1.0 - p)) * (term1 - term2))
