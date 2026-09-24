from reversible_jump_mcmc_model_choice import rjmcmc_acceptance_probability


def test_rjmcmc():
    alpha = rjmcmc_acceptance_probability(1.0, 2.0, 1.0, 1.0, 1.0)
    assert alpha == 1.0
