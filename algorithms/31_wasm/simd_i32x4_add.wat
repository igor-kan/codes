;; simd_i32x4_add.wat -- 128-bit SIMD integer addition.
(module
  (memory (export "memory") 1)
  (func (export "add4") (param $dst i32) (param $a i32) (param $b i32)
    local.get $dst
    local.get $a
    v128.load
    local.get $b
    v128.load
    i32x4.add
    v128.store))
