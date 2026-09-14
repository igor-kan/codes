# Assembly Language

Hand-written, self-contained assembly programs for three instruction-set
architectures. Every file is a complete program that talks to the Linux kernel
through the raw syscall interface (no libc), which makes the instruction flow
easy to read end to end.

| Directory | ISA | Assembler | Syscall ABI |
|:---|:---|:---|:---|
| `x86_64/` | x86-64 | GNU `as` (AT&T, plus one Intel-syntax file) | `syscall`, `rax` + args in `rdi/rsi/rdx` |
| `arm64/` | AArch64 | `clang --target=aarch64-linux-gnu` | `svc #0`, `x8` + args in `x0..x2` |
| `riscv64/` | RV64GC | `clang --target=riscv64-linux-gnu` | `ecall`, `a7` + args in `a0..a2` |

## Examples

| Program | Demonstrates | Result |
|:---|:---|:---|
| `hello_world.s` | write(2) syscall | prints `Hello, …` |
| `exit_42.s` | exit(2) syscall | status 42 |
| `cat.s` | read/write loop | echoes stdin |
| `strlen.s` | pointer walking | exit status = length |
| `sum_array.s` | indexed loads | exit status = sum |
| `fibonacci.s` | register iteration | `fib(10) = 55` |
| `gcd.s` | Euclid's algorithm | `gcd(48,36) = 12` |
| `factorial.s` | integer multiply loop | `5! = 120` |
| `bubble_sort.s` | in-place sort | exit status = minimum |
| `memcpy.s` | byte copy routine | exit status = first byte |
| `memset.s` | byte fill routine | exit status = fill byte |
| `atoi.s` | decimal parsing | exit status = `1234 & 0xff` |
| `itoa_print.s` | decimal formatting | prints `12345` |
| `popcnt.s` | `POPCNT` instruction | 16 |
| `count_ones.s` | Kernighan's bit trick | 6 |
| `sse_sum.s` | SSE2 `paddd` | 11 |
| `cpuid_vendor.s` | `CPUID` leaf 0 | vendor string |
| `rdtsc.s` | timestamp counter | stored to memory |
| `reverse_print.s` | backward iteration | prints `olleH` |
| `is_prime.s` | trial division | status 0 (prime) |
| `binary_search.s` | branchy search | index 5 |
| `int_pow.s` | exponentiation by squaring | `2^5 = 32` |
| `to_upper.s` | byte transforms | prints `HELLO` |
| `min_of_array.s` | conditional moves | exit status = minimum |
| `intel_syntax.s` | `.intel_syntax noprefix` | prints `Hello, Intel!` |

## Build and run

```bash
# x86-64
as --64 x86_64/hello_world.s -o hello_world.o && ld hello_world.o -o hello_world && ./hello_world

# AArch64 (cross-assemble)
clang --target=aarch64-linux-gnu -c arm64/hello_world.s -o hello_world.o

# RISC-V 64 (cross-assemble)
clang --target=riscv64-linux-gnu -c riscv64/hello_world.s -o hello_world.o
```

Conventions: x86-64 files use AT&T syntax; AArch64 files use `//` comments and
`#` immediates; RISC-V files use the standard GNU assembler syntax.
