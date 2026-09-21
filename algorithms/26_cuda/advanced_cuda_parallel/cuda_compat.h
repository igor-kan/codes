#ifndef CUDA_COMPAT_H
#define CUDA_COMPAT_H

#ifndef __CUDACC__
#define __global__
#define __device__
#define __host__
#define __constant__
#define __shared__ static
#define __inline__ inline

struct float3 { float x, y, z; };
inline float3 make_float3(float x, float y, float z) { float3 f = {x, y, z}; return f; }

inline void __syncthreads() {}
#include <math.h>

#endif

#endif
