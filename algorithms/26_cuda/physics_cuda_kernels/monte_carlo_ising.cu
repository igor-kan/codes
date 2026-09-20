#include "monte_carlo_ising.cuh"

__device__ float curand_uniform_fast(unsigned long long* state) {
    *state = (*state * 6364136223846793005ULL + 1442695040888963407ULL);
    return (float)((*state >> 32) & 0xFFFFFF) / 16777216.0f;
}

__global__ void ising_checkerboard_sweep_kernel(
    int8_t* lattice,
    int L,
    float beta,
    int color,
    unsigned long long seed
) {
    int i = blockIdx.y * blockDim.y + threadIdx.y;
    int j = blockIdx.x * blockDim.x + threadIdx.x;

    if (i >= L || j >= L) return;
    if (((i + j) & 1) != color) return;

    int idx = i * L + j;
    int8_t s = lattice[idx];

    int up = ((i - 1 + L) % L) * L + j;
    int down = ((i + 1) % L) * L + j;
    int left = i * L + ((j - 1 + L) % L);
    int right = i * L + ((j + 1) % L);

    int sum_nn = lattice[up] + lattice[down] + lattice[left] + lattice[right];
    int dE = 2 * s * sum_nn;

    unsigned long long rng_state = seed + idx;
    if (dE <= 0 || curand_uniform_fast(&rng_state) < expf(-beta * dE)) {
        lattice[idx] = -s;
    }
}
