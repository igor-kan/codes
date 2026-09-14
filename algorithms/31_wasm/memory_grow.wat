;; memory_grow.wat -- dynamic linear-memory growth.
(module
  (memory (export "memory") 1)
  (func (export "grow") (param $pages i32) (result i32)
    local.get $pages
    memory.grow)
  (func (export "size") (result i32)
    memory.size))
