#pragma once
#include <cuda_runtime.h>

__global__ void nbody_gravitational_forces_kernel(
    const float4* __restrict__ pos_mass,
    float3* __restrict__ accel,
    int n,
    float eps_sq,
    float G = 1.0f
);
