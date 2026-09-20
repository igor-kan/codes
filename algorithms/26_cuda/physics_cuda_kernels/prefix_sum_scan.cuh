#pragma once
#include <cuda_runtime.h>

__global__ void blelloch_work_efficient_scan(float* d_out, const float* d_in, int n);
