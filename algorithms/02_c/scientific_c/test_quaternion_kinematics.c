#include <stdio.h>
#include <assert.h>
#include <math.h>
#include "quaternion_kinematics.h"

int main(void) {
    // 90-degree rotation around z-axis: cos(45) + sin(45)*k
    double s = sin(M_PI / 4.0);
    double c = cos(M_PI / 4.0);
    Quaternion qz = {c, 0.0, 0.0, s};
    double v[3] = {1.0, 0.0, 0.0};
    double v_rot[3];
    quat_rotate_vector(qz, v, v_rot);
    // Should be {0.0, 1.0, 0.0}
    assert(fabs(v_rot[0] - 0.0) < 1e-6);
    assert(fabs(v_rot[1] - 1.0) < 1e-6);
    assert(fabs(v_rot[2] - 0.0) < 1e-6);
    printf("test_quaternion_kinematics PASSED\n");
    return 0;
}
