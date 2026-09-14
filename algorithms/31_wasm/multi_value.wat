;; multi_value.wat -- multiple return values.
(module
  (func (export "divmod") (param $a i32) (param $b i32) (result i32 i32)
    local.get $a
    local.get $b
    i32.div_u
    local.get $a
    local.get $b
    i32.rem_u))
