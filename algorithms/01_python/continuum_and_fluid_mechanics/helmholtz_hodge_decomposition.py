"""
2D Helmholtz-Hodge Vector Field Decomposition.
References: Landau & Lifshitz - Fluid Mechanics.
"""
import numpy as np

def helmholtz_decomposition_2d(u: np.ndarray, v: np.ndarray, dx: float = 1.0, dy: float = 1.0):
    """
    Decompose (u, v) into solenoidal (divergence-free) and irrotational (curl-free) parts in Fourier space.
    """
    ny, nx = u.shape
    kx = 2.0 * np.pi * np.fft.fftfreq(nx, dx)
    ky = 2.0 * np.pi * np.fft.fftfreq(ny, dy)
    KX, KY = np.meshgrid(kx, ky)
    K2 = KX**2 + KY**2
    K2[0, 0] = 1.0  # Avoid div zero

    U_hat = np.fft.fft2(u)
    V_hat = np.fft.fft2(v)

    # Potential phi_hat = -i (kx U + ky V) / K^2
    phi_hat = -1j * (KX * U_hat + KY * V_hat) / K2
    phi_hat[0, 0] = 0.0

    # Irrotational velocity
    U_irr_hat = 1j * KX * phi_hat
    V_irr_hat = 1j * KY * phi_hat

    u_irr = np.fft.ifft2(U_irr_hat).real
    v_irr = np.fft.ifft2(V_irr_hat).real

    u_sol = u - u_irr
    v_sol = v - v_irr
    return (u_sol, v_sol), (u_irr, v_irr)
