# LLVM IR

Low-level LLVM intermediate representation generated from the reference C
implementations in `../02_c/`. This shows the machine-independent IR that the
Clang front end emits before target-specific code generation, and provides a
readable bridge between the C sources and the assembly in `../27_assembly/`.

## Generate

Every `.ll` file here is produced with:

```bash
clang -O2 -S -emit-llvm -w algorithms/02_c/<category>/<name>.c -o algorithms/30_llvm_ir/<category>/<name>.ll
```

## Verify and execute

```bash
opt -passes=verify -disable-output algorithms/30_llvm_ir/graphs/dijkstra.ll   # validate
llvm-as algorithms/30_llvm_ir/math/gcd.ll -o gcd.bc                           # assemble
lli gcd.bc                                                                    # interpret
opt -O3 -S algorithms/30_llvm_ir/sorting/quick_sort.ll -o quick_sort.opt.ll   # optimize
```

## Layout

| Directory | Mirrors |
|:---|:---|
| `data_structures/` | `02_c/data_structures/` |
| `dp/` | `02_c/dp/` |
| `graphs/` | `02_c/graphs/` |
| `math/` | `02_c/math/` |
| `searching/` | `02_c/searching/` |
| `sorting/` | `02_c/sorting/` |
| `strings/` | `02_c/strings/` |
| `techniques/` | `02_c/techniques/` |

The IR is compiler output, not hand-written; regenerate rather than edit.
