;; fibonacci.wat -- iterative Fibonacci.
(module
  (func (export "fib") (param $n i32) (result i32)
    (local $a i32)
    (local $b i32)
    (local $t i32)
    i32.const 0
    local.set $a
    i32.const 1
    local.set $b
    block $done
      loop $loop
        local.get $n
        i32.eqz
        br_if $done
        local.get $a
        local.get $b
        i32.add
        local.set $t
        local.get $b
        local.set $a
        local.get $t
        local.set $b
        local.get $n
        i32.const 1
        i32.sub
        local.set $n
        br $loop
      end
    end
    local.get $a))
