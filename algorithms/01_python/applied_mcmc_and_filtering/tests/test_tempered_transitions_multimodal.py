import numpy as np
from tempered_transitions_multimodal import geometric_temperature_ladder


def test_ladder():
    ladder = geometric_temperature_ladder(5, 0.1, 1.0)
    assert len(ladder) == 5
    assert np.all(np.diff(ladder) > 0.0)
