import os
import sys
import numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from mcmc_diagnostics import gelman_rubin_rhat

def test_rhat_converged():
    np.random.seed(42)
    # 4 independent chains from N(0, 1) should have R-hat close to 1.0
    chains = np.random.normal(size=(4, 1000))
    rhat = gelman_rubin_rhat(chains)
    assert np.isclose(rhat, 1.0, atol=0.05)
