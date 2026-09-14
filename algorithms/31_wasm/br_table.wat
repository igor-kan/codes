;; br_table.wat -- multi-way branching (jump table).
(module
  (func (export "classify") (param $x i32) (result i32)
    block $default
      block $case2
        block $case1
          block $case0
            local.get $x
            br_table $case0 $case1 $case2 $default
          end
          i32.const 10
          return
        end
        i32.const 20
        return
      end
      i32.const 30
      return
    end
    i32.const -1))
