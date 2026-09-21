#include "monte_carlo_pi.h"

static unsigned long lcg_next(unsigned long *state) {
    *state = (*state * 6364136223846793005ULL + 1ULL);
    return *state;
}

double estimate_pi_monte_carlo(unsigned long num_samples, unsigned long seed) {
    unsigned long state = seed;
    unsigned long inside = 0;
    const double inv = 1.0 / 18446744073709551616.0;
    
    for (unsigned long i = 0; i < num_samples; ++i) {
        double x = (double)lcg_next(&state) * inv;
        double y = (double)lcg_next(&state) * inv;
        if (x * x + y * y <= 1.0) {
            inside++;
        }
    }
    return 4.0 * (double)inside / (double)num_samples;
}
