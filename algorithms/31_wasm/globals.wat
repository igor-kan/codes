;; globals.wat -- mutable module state.
(module
  (global $counter (mut i32) (i32.const 0))
  (global $limit i32 (i32.const 100))
  (func (export "next") (result i32)
    global.get $counter
    i32.const 1
    i32.add
    global.set $counter
    global.get $counter)
  (func (export "at_limit") (result i32)
    global.get $counter
    global.get $limit
    i32.ge_s))
