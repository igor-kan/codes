;; f32_ops.wat -- scalar floating-point arithmetic.
(module
  (func (export "saxpy") (param $a f32) (param $x f32) (param $y f32) (result f32)
    local.get $a
    local.get $x
    f32.mul
    local.get $y
    f32.add)
  (func (export "dist") (param $x f32) (param $y f32) (result f32)
    local.get $x
    local.get $x
    f32.mul
    local.get $y
    local.get $y
    f32.mul
    f32.add
    f32.sqrt))
