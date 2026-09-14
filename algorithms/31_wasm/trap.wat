;; trap.wat -- arithmetic that traps on division by zero.
(module
  (func (export "div") (param $a i32) (param $b i32) (result i32)
    local.get $a
    local.get $b
    i32.div_s)
  (func (export "unreachable_") (result i32)
    unreachable))
