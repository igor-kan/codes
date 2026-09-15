/* Composite Simpson's rule (Numerical Recipes 4.1). */
#include <assert.h>
#include <math.h>
#include <stdio.h>

static double simpson(double (*f)(double), double a, double b, int n) {
    if (n % 2) n++;
    double h = (b - a) / n, total = f(a) + f(b);
    for (int i = 1; i < n; ++i) total += (i % 2 ? 4.0 : 2.0) * f(a + i * h);
    return total * h / 3.0;
}

static double square(double x) { return x * x; }

int main(void) {
    assert(fabs(simpson(square, 0, 1, 1000) - 1.0 / 3) < 1e-12);
    printf("simpson integration ok\n");
    return 0;
}
