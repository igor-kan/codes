import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from deflated_sharpe_ratio import deflated_sharpe_ratio

def test_dsr():
    # Observed SR = 2.5 after 100 trials
    p = deflated_sharpe_ratio(sr_observed=2.5, n_trials=10, var_sr_trials=0.1, t_observations=252)
    assert 0.0 <= p <= 1.0
