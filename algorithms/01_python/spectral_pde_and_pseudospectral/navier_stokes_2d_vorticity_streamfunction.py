"""2D Incompressible Navier-Stokes Vorticity-Streamfunction Formulation."""
import numpy as np


def solve_streamfunction_poisson_fft(omega: np.ndarray, Lx: float, Ly: float) -> np.ndarray:
    """Invert Laplacian psi_xx + psi_yy = -omega via 2D FFT."""
    Ny, Nx = omega.shape
    kx = 2.0 * np.pi * np.fft.fftfreq(Nx, d=Lx / Nx)
    ky = 2.0 * np.pi * np.fft.fftfreq(Ny, d=Ly / Ny)
    KX, KY = np.meshgrid(kx, ky)
    K_sq = KX**2 + KY**2
    K_sq[0, 0] = 1.0  # Regularize zero mode
    
    omega_hat = np.fft.fft2(omega)
    psi_hat = omega_hat / K_sq
    psi_hat[0, 0] = 0.0
    return np.real(np.fft.ifft2(psi_hat))
