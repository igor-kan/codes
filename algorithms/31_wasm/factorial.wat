;; factorial.wat -- iterative factorial.
(module
  (func (export "factorial") (param $n i32) (result i32)
    (local $i i32)
    (local $acc i32)
    i32.const 1
    local.set $acc
    i32.const 1
    local.set $i
    block $done
      loop $loop
        local.get $i
        local.get $n
        i32.gt_u
        br_if $done
        local.get $acc
        local.get $i
        i32.mul
        local.set $acc
        local.get $i
        i32.const 1
        i32.add
        local.set $i
        br $loop
      end
    end
    local.get $acc))
