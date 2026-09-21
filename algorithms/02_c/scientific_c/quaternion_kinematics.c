#include "quaternion_kinematics.h"

Quaternion quat_multiply(Quaternion q1, Quaternion q2) {
    Quaternion r;
    r.w = q1.w*q2.w - q1.x*q2.x - q1.y*q2.y - q1.z*q2.z;
    r.x = q1.w*q2.x + q1.x*q2.w + q1.y*q2.z - q1.z*q2.y;
    r.y = q1.w*q2.y - q1.x*q2.z + q1.y*q2.w + q1.z*q2.x;
    r.z = q1.w*q2.z + q1.x*q2.y - q1.y*q2.x + q1.z*q2.w;
    return r;
}

void quat_rotate_vector(Quaternion q, const double v[3], double v_out[3]) {
    Quaternion p = {0.0, v[0], v[1], v[2]};
    Quaternion q_conj = {q.w, -q.x, -q.y, -q.z};
    Quaternion res = quat_multiply(quat_multiply(q, p), q_conj);
    v_out[0] = res.x;
    v_out[1] = res.y;
    v_out[2] = res.z;
}
