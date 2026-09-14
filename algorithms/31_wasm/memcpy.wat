;; memcpy.wat -- linear-memory copy via the bulk memory.copy instruction.
(module
  (memory (export "memory") 1)
  (func (export "memcpy") (param $dst i32) (param $src i32) (param $n i32)
    local.get $dst
    local.get $src
    local.get $n
    memory.copy))
