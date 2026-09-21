#ifndef MONTE_CARLO_OPTION_PRICING_CUH
#define MONTE_CARLO_OPTION_PRICING_CUH

__global__ void mc_european_call_kernel(float* d_payoffs, float S0, float K, float r, float v, float T, int n_paths);

#endif
