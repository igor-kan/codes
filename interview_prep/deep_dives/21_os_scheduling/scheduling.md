# CPU Scheduling

## Metrics

- **Turnaround time** = completion − arrival.
- **Response time** = first run − arrival.
- **Throughput**, **fairness**, **waiting time**, **CPU utilization**.

## Policies

| Policy | Rule | Notes |
|:---|:---|:---|
| FIFO | arrival order | convoy effect |
| SJF | shortest job first | optimal turnaround, needs knowledge |
| STCF | preemptive shortest-to-completion | optimal turnaround |
| Round Robin | time slice, rotate | good response, quantum trade-off |
| MLFQ | feedback by behaviour | learns interactive vs batch |
| Lottery/Stride | proportional share | probabilistic fairness |
| CFS | virtual runtime, RB-tree | Linux default |
| EDF/RM | deadlines | real-time systems |

## MLFQ rules

1. Higher priority runs first.
2. Equal priority → round robin.
3. New jobs enter at the top.
4. Exhausting a quantum demotes.
5. Periodically boost all jobs to the top (prevents starvation).

## Multi-CPU

Per-CPU run queues, load balancing, cache/affinity awareness, and synchronization
of scheduler data. NUMA locality matters.
