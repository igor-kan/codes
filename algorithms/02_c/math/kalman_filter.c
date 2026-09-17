/**
 * 1D Kalman Filter in C (Numerical Recipes 3rd Ed. Chapter 15)
 */

#include <stdio.h>
#include <math.h>
#include <assert.h>

typedef struct {
    double x, p, q, r;
} KalmanFilter1D;

void kf_predict(KalmanFilter1D* kf) {
    kf->p += kf->q;
}

double kf_update(KalmanFilter1D* kf, double z) {
    double k = kf->p / (kf->p + kf->r);
    kf->x += k * (z - kf->x);
    kf->p = (1.0 - k) * kf->p;
    return kf->x;
}

int main(void) {
    KalmanFilter1D kf = {0.0, 1.0, 0.01, 0.1};
    double measurements[] = {0.9, 1.1, 0.95, 1.05};
    for (int i = 0; i < 4; i++) {
        kf_predict(&kf);
        kf_update(&kf, measurements[i]);
    }
    assert(fabs(kf.x - 1.0) < 0.2);
    printf("C Kalman Filter verified.\n");
    return 0;
}
