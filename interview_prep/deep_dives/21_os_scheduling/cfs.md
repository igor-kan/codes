# Completely Fair Scheduler (Linux)

CFS models an ideal fair CPU by tracking **virtual runtime** (`vruntime`) and
always running the task with the smallest value.

## Mechanism

- Each task accumulates `vruntime += runtime / weight`, where weight derives
  from `nice` value.
- Runnable tasks live in a red-black tree keyed by `vruntime`.
- The leftmost node is the next to run.
- `target_latency` and `min_granularity` bound the scheduling period.

## Nice values

Lower nice → higher weight → slower `vruntime` growth → more CPU. The default
nice gives weight 1024; each step ≈ 1.25x CPU share.

## Preemption

A task is preempted when its `vruntime` falls behind the current task's by a
threshold, or when a woken task has a smaller `vruntime`.

## Fairness group scheduling

CFS can distribute CPU between cgroups proportionally, which underpins
containers and QoS.
