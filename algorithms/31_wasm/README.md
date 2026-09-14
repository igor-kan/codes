# WebAssembly Text (WAT)

Hand-written WebAssembly modules in the standard text format. They exercise the
core MVP plus commonly available proposals: bulk memory, reference types,
multi-value and fixed-width (128-bit) SIMD.

## Validate and run

The files are validated with the `wasmtime` Python bindings; any standard
toolchain works:

```bash
wat2wasm add.wat -o add.wasm          # wabt
wasmtime run add.wasm                 # runtime
wasm2wat add.wasm                      # round-trip
```

```python
from wasmtime import wat2wasm, Module, Store, Instance
wasm = wat2wasm(open("add.wat").read())
```

## Examples

| File | Demonstrates |
|:---|:---|
| `add.wat` | minimal exported function |
| `factorial.wat` | `block`/`loop`/`br_if` control flow |
| `fibonacci.wat` | register-style iteration |
| `sum_array.wat` | linear memory, `i32.load`, scaled addressing |
| `gcd.wat` | Euclid's algorithm |
| `is_prime.wat` | early `return` from nested blocks |
| `memcpy.wat` | `memory.copy` (bulk memory proposal) |
| `strlen.wat` | `i32.load8_u` and NUL scanning |
| `bubble_sort.wat` | nested loops over linear memory |
| `f32_ops.wat` | scalar float arithmetic, `f32.sqrt` |
| `simd_i32x4_add.wat` | `v128.load`, `i32x4.add`, `v128.store` |
| `table_call_indirect.wat` | `call_indirect` through `funcref` table |
| `globals.wat` | mutable and immutable globals |
| `memory_grow.wat` | `memory.grow` / `memory.size` |
| `multi_value.wat` | multiple return values |
| `select.wat` | branchless min/max via `select` |
| `br_table.wat` | jump-table dispatch |
| `trap.wat` | trapping instructions and `unreachable` |

Reference: *WebAssembly Core Specification*, W3C
(https://webassembly.github.io/spec/core/).
