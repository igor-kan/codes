from markov_switching_regime_autoregression import two_state_markov_transition_step


def test_markov_step():
    p_next = two_state_markov_transition_step(0.5, p11=0.9, p22=0.8)
    # 0.5 * 0.9 + 0.5 * 0.2 = 0.45 + 0.10 = 0.55
    assert p_next == 0.55
