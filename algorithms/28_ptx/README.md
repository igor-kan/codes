# PTX (Parallel Thread Execution)

Standalone PTX kernels for the NVIDIA GPU virtual ISA. PTX is the portable,
textual intermediate representation emitted by `nvcc`/`clang` and consumed by
`ptxas`; it sits *above* SASS in the toolchain:

```
CUDA C++  --(nvcc/nvvm)-->  PTX  --(ptxas)-->  SASS  --(GPU)-->  execution
```

These files are written against PTX ISA 8.x (Hopper / `sm_90`) and mirror the
kernels in `26_cuda/` and `29_sass/`.

| File | Focus |
|:---|:---|
| `vector_add.ptx` | thread indexing, `ld.global` / `st.global` |
| `saxpy.ptx` | `fma.rn.f32` |
| `fma.ptx` | vectorized `ld.global.v2.f32` |
| `reduction_sum.ptx` | shared memory, `bar.sync`, tree reduction |
| `matrix_mul_tiled.ptx` | tiled shared-memory matrix multiply |
| `warp_vote.ptx` | `vote.ballot.sync`, `vote.any` |
| `warp_shuffle.ptx` | `shfl.sync.down` prefix sum |
| `atomic_add.ptx` | `atom.global.*`, `red.global.*` |
| `memset.ptx` | `st.global.u8` |
| `memcpy.ptx` | `ld/st.global.v4.u32` |
| `popcount.ptx` | `popc`, `clz`, `brev`, `bfind` |
| `clock_sm.ptx` | `%clock`, `%smid`, `%globaltimer` |
| `special_regs.ptx` | `%tid`, `%ntid`, `%ctaid`, `%laneid`, `%warpid` |
| `predicates.ptx` | `setp`, predicated execution, `and.pred` |
| `vector_types.ptx` | `.v2` / `.v4` vector memory operations |
| `cp_async.ptx` | `cp.async.cg.shared.global`, commit/wait groups |
| `cvt_precision.ptx` | numeric conversions and rounding modes |
| `bar_sync.ptx` | block-level barriers and shared memory |
| `grid_stride.ptx` | grid-stride loop |
| `integer_ops.ptx` | `mul.lo/hi`, `mad.lo`, `div`, shifts, bitwise |

## Assemble

The CUDA Toolkit is required (`ptxas` ships with it); there is no standalone
open-source PTX assembler.

```bash
ptxas -arch=sm_90 vector_add.ptx
nvdisasm -c vector_add.cubin      # inspect the resulting SASS
```

Reference: *Parallel Thread Execution ISA*, NVIDIA
(https://docs.nvidia.com/cuda/parallel-thread-execution/).
