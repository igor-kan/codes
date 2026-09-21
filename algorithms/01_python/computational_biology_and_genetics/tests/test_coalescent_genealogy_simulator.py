import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from coalescent_genealogy_simulator import simulate_coalescent_times

def test_coalescent_length():
    times = simulate_coalescent_times(sample_size=5, N_e=1000)
    assert len(times) == 4  # 4 coalescent events from 5 to 1 lineage
    assert all(t > 0 for t in times)
