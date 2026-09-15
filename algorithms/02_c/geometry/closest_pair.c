/* Closest pair of points (quadratic brute force). */
#include <stdio.h>
#include <math.h>
int main(void) {
    double x[] = {2, 12, 40, 5, 12, 3}, y[] = {3, 30, 50, 1, 10, 4};
    int n = 6;
    double best = 1e18;
    for (int i = 0; i < n; i++)
        for (int j = i + 1; j < n; j++) {
            double d = hypot(x[i] - x[j], y[i] - y[j]);
            if (d < best) best = d;
        }
    if (fabs(best - sqrt(2)) > 1e-9) return 1;
    printf("closest=%g\n", best);
    return 0;
}
