"""
Nuclear Shell Model Single-Particle Energy Levels and Magic Numbers.
References: Kenneth S. Krane - Introductory Nuclear Physics (Ch. 5).
"""
import numpy as np

MAGIC_NUMBERS = [2, 8, 20, 28, 50, 82, 126]

def is_magic_nucleus(Z: int, N: int) -> bool:
    """Check if nucleus is magic or doubly-magic."""
    return (Z in MAGIC_NUMBERS) or (N in MAGIC_NUMBERS)

def is_doubly_magic(Z: int, N: int) -> bool:
    """Check if both Z and N are magic numbers."""
    return (Z in MAGIC_NUMBERS) and (N in MAGIC_NUMBERS)
