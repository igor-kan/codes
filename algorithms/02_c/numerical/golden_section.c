/* Golden-section search for a 1D minimum (Numerical Recipes 10.1). */
#include <assert.h>
#include <math.h>
#include <stdio.h>

static double f(double x) { return (x - 3) * (x - 3); }

int main(void) {
    double a = -10, b = 10, invPhi = (sqrt(5.0) - 1) / 2;
    double c = b - invPhi * (b - a), d = a + invPhi * (b - a);
    double fc = f(c), fd = f(d);
    while (b - a > 1e-9) {
        if (fc < fd) { b = d; d = c; fd = fc; c = b - invPhi * (b - a); fc = f(c); }
        else { a = c; c = d; fc = fd; d = a + invPhi * (b - a); fd = f(d); }
    }
    assert(fabs((a + b) / 2 - 3) < 1e-6);
    printf("golden section ok\n");
    return 0;
}
