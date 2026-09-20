"""
Cylindrical Bessel Functions via Miller's Algorithm and Series.
References: Riley, Hobson, Bence - Mathematical Methods for Physics and Engineering.
"""
import numpy as np
import math

def bessel_j0(x: float) -> float:
    """Evaluate J_0(x) using power series / asymptotic expansion."""
    ax = abs(x)
    if ax < 8.0:
        y = x * x
        ans1 = 57568490574.0 + y * (-13362590354.0 + y * (651619640.7
               + y * (-11214424.18 + y * (77392.33017 + y * (-184.9052456)))))
        ans2 = 57568490411.0 + y * (1029532985.0 + y * (9494680.718
               + y * (59272.64853 + y * (267.8532712 + y * 1.0))))
        return ans1 / ans2
    else:
        z = 8.0 / ax
        y = z * z
        xx = ax - 0.785398164
        ans1 = 1.0 + y * (-0.1098628627e-2 + y * (0.2734510407e-4
               + y * (-0.2073370639e-5 + y * 0.2093887211e-6)))
        ans2 = -0.1562499995e-1 + y * (0.1430488765e-3
               + y * (-0.6911147651e-5 + y * (0.7621095161e-6 - y * 0.934945152e-7)))
        return np.sqrt(0.636619772 / ax) * (np.cos(xx) * ans1 - z * np.sin(xx) * ans2)

def bessel_jn_miller(n: int, x: float, m_start: int = 40) -> float:
    """Evaluate J_n(x) using Miller's backward recurrence."""
    if x == 0.0:
        return 1.0 if n == 0 else 0.0
    if abs(x) > m_start:
        m_start = int(abs(x)) + 30
    
    # Miller backward recurrence
    b = np.zeros(m_start + 2)
    b[m_start + 1] = 0.0
    b[m_start] = 1.0
    for k in range(m_start - 1, -1, -1):
        b[k] = (2.0 * (k + 1) / x) * b[k + 1] - b[k + 2]
    
    # Normalization: J_0 + 2 J_2 + 2 J_4 + ... = 1
    norm = b[0] + 2.0 * np.sum(b[2::2])
    return float(b[n] / norm)
