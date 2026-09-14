;; table_call_indirect.wat -- indirect calls through a function table.
(module
  (type $binop (func (param i32 i32) (result i32)))
  (func $add (type $binop) local.get 0 local.get 1 i32.add)
  (func $sub (type $binop) local.get 0 local.get 1 i32.sub)
  (func $mul (type $binop) local.get 0 local.get 1 i32.mul)
  (table 3 funcref)
  (elem (i32.const 0) $add $sub $mul)
  (func (export "apply") (param $op i32) (param $a i32) (param $b i32) (result i32)
    local.get $a
    local.get $b
    local.get $op
    call_indirect (type $binop)))
