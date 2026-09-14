;; is_prime.wat -- trial-division primality test.
(module
  (func (export "is_prime") (param $n i32) (result i32)
    (local $i i32)
    local.get $n
    i32.const 2
    i32.lt_s
    if
      i32.const 0
      return
    end
    i32.const 2
    local.set $i
    block $done
      loop $loop
        local.get $i
        local.get $i
        i32.mul
        local.get $n
        i32.gt_s
        br_if $done
        local.get $n
        local.get $i
        i32.rem_s
        i32.eqz
        if
          i32.const 0
          return
        end
        local.get $i
        i32.const 1
        i32.add
        local.set $i
        br $loop
      end
    end
    i32.const 1))
