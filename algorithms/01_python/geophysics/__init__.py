"""Geophysics, Seismology & Geodynamics Package.

Algorithms for elastic wave propagation, earthquake mechanics, isostasy, gravity anomalies, geomagnetism, and thermal mantle convection.
"""

from .seismic_wave_speeds import SeismicWaveSpeeds
from .snells_law_seismic_refraction import SeismicRefraction
from .seismic_reflection_nmo import SeismicReflectionNMO
from .earthquake_moment_magnitude import MomentMagnitude
from .gutenberg_richter_law import GutenbergRichterLaw
from .omori_aftershock_law import OmoriLaw
from .airy_pratt_isostasy import IsostasyModels
from .gravitational_bouguer_anomaly import GravityAnomalies
from .geomagnetic_dipole_field import GeomagneticDipole
from .heat_flow_geotherm import ContinentalGeotherm
from .oceanic_crust_cooling_halfspace import OceanicLithosphereCooling
from .chandler_wobble_euler import EarthPrecession
from .rayleigh_love_surface_waves import SurfaceWaves
from .focal_mechanism_beachball import FocalMechanism
from .mantle_convection_rayleigh_benard import MantleConvection

__all__ = [
    "SeismicWaveSpeeds",
    "SeismicRefraction",
    "SeismicReflectionNMO",
    "MomentMagnitude",
    "GutenbergRichterLaw",
    "OmoriLaw",
    "IsostasyModels",
    "GravityAnomalies",
    "GeomagneticDipole",
    "ContinentalGeotherm",
    "OceanicLithosphereCooling",
    "EarthPrecession",
    "SurfaceWaves",
    "FocalMechanism",
    "MantleConvection",
]
