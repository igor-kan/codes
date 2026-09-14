# SASS Reference Listings

SASS (Shader Assembly) is the low-level machine ISA executed by NVIDIA GPUs.
It is not a portable assembly language: the exact instruction encoding and
opcode set are specific to each GPU generation, and NVIDIA does not publish a
public SASS assembler.

These files are **hand-annotated reference listings** written from public
NVIDIA documentation and the `nvdisasm`/`cuobjdump` binary-utilities reference.
They illustrate the SASS emitted for small CUDA kernels targeting the
**sm_90 (Hopper)** architecture. They are intended for study alongside the
CUDA and PTX implementations in this repository, not for assembly.

To produce SASS for your own kernels:

```bash
nvcc -arch=sm_90 -cubin kernel.cu -o kernel.cubin
nvdisasm -c -g kernel.cubin             # control flow + source line info
nvdisasm -c -plr kernel.cubin           # per-instruction register usage
cuobjdump -sass kernel.cubin            # raw SASS dump
```

Key instruction families used below:

| Family | Examples | Meaning |
|:---|:---|:---|
| Control | `BRA`, `EXIT`, `BSSY`/`BSYNC` | branches, exit, convergence barriers |
| Integer | `IMAD`, `IADD3`, `LOP3`, `SHF`, `ISETP` | multiply-add, add, logic, funnel shift, integer compare |
| Memory | `LDG`, `STG`, `LDS`, `STS`, `LDC` | global / shared / constant memory |
| Float | `FADD`, `FFMA`, `FMUL`, `FSETP` | FP32 arithmetic and compare |
| Move | `MOV`, `S2R`, `S2UR` | register/constant moves, special-register reads |
| Control bits | `@P0`, `!PT` | predicate guards and predicate-true register |

Instruction scheduling and dual-issue are encoded in the (uppercase) control
bits following many SASS instructions; they are omitted here for readability.
