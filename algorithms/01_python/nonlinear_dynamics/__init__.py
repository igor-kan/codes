"""Nonlinear Dynamics, Solitons & Chaos Package.

Algorithms for strange attractors, Lyapunov spectra, solitons, synchronization, and bifurcations.
"""

from .lorenz_attractor_rk4 import LorenzAttractor
from .rossler_attractor import RosslerAttractor
from .lyapunov_exponent_spectrum import LyapunovExponent
from .korteveg_de_vries_soliton import KdVSoliton
from .sine_gordon_kink_breather import SineGordonSoliton
from .nonlinear_schrodinger_soliton import NLSESoliton
from .kuramoto_oscillators_sync import KuramotoModel
from .hopf_bifurcation import HopfBifurcation
from .pitchfork_transcritical_bifurcations import BifurcationNormalForms
from .duffing_chaotic_oscillator import DuffingOscillator
from .van_der_pol_relaxation import VanDerPolOscillator
from .feigenbaum_bifurcation_tree import FeigenbaumCascade
from .fractal_box_counting_dimension import BoxCountingDimension
from .takens_delay_embedding import TakensEmbedding
from .arnold_cat_map import ArnoldCatMap

__all__ = [
    "LorenzAttractor",
    "RosslerAttractor",
    "LyapunovExponent",
    "KdVSoliton",
    "SineGordonSoliton",
    "NLSESoliton",
    "KuramotoModel",
    "HopfBifurcation",
    "BifurcationNormalForms",
    "DuffingOscillator",
    "VanDerPolOscillator",
    "FeigenbaumCascade",
    "BoxCountingDimension",
    "TakensEmbedding",
    "ArnoldCatMap",
]
