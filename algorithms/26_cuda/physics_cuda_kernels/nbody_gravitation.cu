#include "nbody_gravitation.cuh"

__global__ void nbody_gravitational_forces_kernel(
    const float4* __restrict__ pos_mass,
    float3* __restrict__ accel,
    int n,
    float eps_sq,
    float G
) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i >= n) return;

    float4 pi = pos_mass[i];
    float3 ai = make_float3(0.0f, 0.0f, 0.0f);

    for (int j = 0; j < n; ++j) {
        if (i == j) continue;
        float4 pj = pos_mass[j];
        float dx = pj.x - pi.x;
        float dy = pj.y - pi.y;
        float dz = pj.z - pi.z;
        float dist_sq = dx * dx + dy * dy + dz * dz + eps_sq;
        float inv_dist = rsqrtf(dist_sq);
        float inv_dist3 = inv_dist * inv_dist * inv_dist;
        float s = G * pj.w * inv_dist3;
        ai.x += s * dx;
        ai.y += s * dy;
        ai.z += s * dz;
    }
    accel[i] = ai;
}
