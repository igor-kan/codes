;; sum_array.wat -- sum `len` i32 values starting at `ptr`.
(module
  (memory (export "memory") 1)
  (func (export "sum") (param $ptr i32) (param $len i32) (result i32)
    (local $i i32)
    (local $acc i32)
    block $done
      loop $loop
        local.get $i
        local.get $len
        i32.ge_u
        br_if $done
        local.get $acc
        local.get $ptr
        local.get $i
        i32.const 4
        i32.mul
        i32.add
        i32.load
        i32.add
        local.set $acc
        local.get $i
        i32.const 1
        i32.add
        local.set $i
        br $loop
      end
    end
    local.get $acc))
