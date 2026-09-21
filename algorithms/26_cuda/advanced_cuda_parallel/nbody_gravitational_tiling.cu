#include "nbody_gravitational_tiling.cuh"
#include <math.h>

#define NBODY_TILE 256

__global__ void nbody_tiled_accel_kernel(float3* d_acc, const BodyPos* d_pos, int n) {
    __shared__ BodyPos sh_pos[NBODY_TILE];
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    float3 acc = make_float3(0.0f, 0.0f, 0.0f);
    
    for (int tile = 0; tile < (n + NBODY_TILE - 1) / NBODY_TILE; ++tile) {
        int idx = tile * NBODY_TILE + threadIdx.x;
        if (idx < n) sh_pos[threadIdx.x] = d_pos[idx];
        __syncthreads();
        
        for (int j = 0; j < NBODY_TILE; ++j) {
            float dx = sh_pos[j].x - (i < n ? d_pos[i].x : 0);
            float dy = sh_pos[j].y - (i < n ? d_pos[i].y : 0);
            float dz = sh_pos[j].z - (i < n ? d_pos[i].z : 0);
            float dist_sq = dx*dx + dy*dy + dz*dz + 1e-6f;
            float inv_dist = rsqrtf(dist_sq);
            float inv_dist3 = inv_dist * inv_dist * inv_dist;
            acc.x += sh_pos[j].m * dx * inv_dist3;
        }
        __syncthreads();
    }
    if (i < n) d_acc[i] = acc;
}
