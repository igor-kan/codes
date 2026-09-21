#ifndef QUATERNION_KINEMATICS_H
#define QUATERNION_KINEMATICS_H

typedef struct {
    double w, x, y, z;
} Quaternion;

Quaternion quat_multiply(Quaternion q1, Quaternion q2);
void quat_rotate_vector(Quaternion q, const double v_in[3], double v_out[3]);

#endif
