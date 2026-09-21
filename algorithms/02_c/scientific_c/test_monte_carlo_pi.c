#include <stdio.h>
#include <assert.h>
#include <math.h>
#include "monte_carlo_pi.h"

int main(void) {
    double pi_est = estimate_pi_monte_carlo(1000000, 12345ULL);
    assert(fabs(pi_est - M_PI) < 0.01);
    printf("test_monte_carlo_pi PASSED\n");
    return 0;
}
