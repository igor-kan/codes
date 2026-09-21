#include "monte_carlo_option_pricing.cuh"
#include <math.h>

__global__ void mc_european_call_kernel(float* d_payoffs, float S0, float K, float r, float v, float T, int n_paths) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < n_paths) {
        float drift = (r - 0.5f * v * v) * T;
        float diffusion = v * sqrtf(T) * 0.0f; // placeholder random norm
        float ST = S0 * expf(drift + diffusion);
        d_payoffs[idx] = fmaxf(0.0f, ST - K);
    }
}
