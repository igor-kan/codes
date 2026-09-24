import numpy as np
from watson_lemma_laplace_integrals import watson_lemma_leading_term


def test_watson():
    val = watson_lemma_leading_term(alpha=1.0, c0=1.0, lam=2.0)
    # Gamma(2) / 4 = 1/4 = 0.25
    assert val == 0.25
