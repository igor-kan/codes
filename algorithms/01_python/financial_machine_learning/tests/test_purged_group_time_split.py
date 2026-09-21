import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from purged_group_time_split import purged_train_test_split

def test_purging():
    train, test = purged_train_test_split(n_samples=100, test_start=40, test_end=60, purge_window=5, embargo_window=5)
    assert 34 in train
    assert 35 not in train  # Purged
    assert 64 not in train  # Embargoed
    assert 65 in train
