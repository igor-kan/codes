;; strlen.wat -- length of a NUL-terminated string.
(module
  (memory (export "memory") 1)
  (func (export "strlen") (param $ptr i32) (result i32)
    (local $i i32)
    block $done
      loop $loop
        local.get $ptr
        local.get $i
        i32.add
        i32.load8_u
        i32.eqz
        br_if $done
        local.get $i
        i32.const 1
        i32.add
        local.set $i
        br $loop
      end
    end
    local.get $i))
