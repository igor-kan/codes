import os, sys, numpy as np
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from takens_delay_embedding import delay_embed_1d

def test_delay_embed():
    ts = np.arange(10, dtype=float)
    emb = delay_embed_1d(ts, embedding_dim=3, delay=2)
    # Row 0: [0, 2, 4]
    assert np.allclose(emb[0], [0.0, 2.0, 4.0])
