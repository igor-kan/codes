import numpy as np
from nekhoroshev_stability import nekhoroshev_stability_time


def test_nekhoroshev():
    # As perturbation epsilon decreases, stability time grows exponentially
    t1 = nekhoroshev_stability_time(0.01)
    t2 = nekhoroshev_stability_time(0.001)
    assert t2 > t1
