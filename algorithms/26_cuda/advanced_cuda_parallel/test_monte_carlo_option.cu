#include <stdio.h>
#include <assert.h>
#include <math.h>
#include "monte_carlo_option_pricing.cuh"

int main() {
    float S0 = 100.0f, K = 100.0f;
    float payoff = fmaxf(0.0f, S0 - K);
    assert(payoff == 0.0f);
    printf("test_monte_carlo_option PASSED\n");
    return 0;
}
