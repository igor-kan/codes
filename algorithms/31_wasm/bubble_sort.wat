;; bubble_sort.wat -- in-place bubble sort of an i32 array.
(module
  (memory (export "memory") 1)
  (func (export "bubble_sort") (param $ptr i32) (param $len i32)
    (local $i i32)
    (local $j i32)
    (local $a i32)
    (local $b i32)
    (local $addr i32)
    block $outer_done
      loop $outer
        local.get $i
        local.get $len
        i32.ge_u
        br_if $outer_done
        i32.const 0
        local.set $j
        block $inner_done
          loop $inner
            local.get $j
            i32.const 1
            i32.add
            local.get $len
            local.get $i
            i32.sub
            i32.ge_u
            br_if $inner_done
            local.get $ptr
            local.get $j
            i32.const 4
            i32.mul
            i32.add
            local.set $addr
            local.get $addr
            i32.load
            local.set $a
            local.get $addr
            i32.load offset=4
            local.set $b
            local.get $a
            local.get $b
            i32.gt_s
            if
              local.get $addr
              local.get $b
              i32.store
              local.get $addr
              local.get $a
              i32.store offset=4
            end
            local.get $j
            i32.const 1
            i32.add
            local.set $j
            br $inner
          end
        end
        local.get $i
        i32.const 1
        i32.add
        local.set $i
        br $outer
      end
    end))
