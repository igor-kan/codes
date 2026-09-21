#ifndef NBODY_GRAVITATIONAL_TILING_CUH
#define NBODY_GRAVITATIONAL_TILING_CUH

struct BodyPos {
    float x, y, z, m;
};

__global__ void nbody_tiled_accel_kernel(float3* d_acc, const BodyPos* d_pos, int n);

#endif
