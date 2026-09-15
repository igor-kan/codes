#include <assert.h>
#include <math.h>
#include <stdio.h>

static double acceleration(double x) { return -x; }

static double verlet(double x, double v, double dt, int steps, double *vout) {
    for (int i = 0; i < steps; ++i) {
        double a = acceleration(x);
        double x_new = x + v * dt + 0.5 * a * dt * dt;
        double a_new = acceleration(x_new);
        v = v + 0.5 * (a + a_new) * dt;
        x = x_new;
    }
    *vout = v;
    return x;
}

int main(void) {
    double velocity;
    double position = verlet(1.0, 0.0, 0.001, 10000, &velocity);
    double energy = 0.5 * (velocity * velocity + position * position);
    assert(fabs(energy - 0.5) < 1e-3);
    assert(fabs(position - cos(10.0)) < 1e-2);
    printf("verlet ok\n");
    return 0;
}
