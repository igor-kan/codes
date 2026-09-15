# Deep Dives

Focused, numbered deep dives into the C++, networking and operating-systems
topics from the study plan. Each directory is self-contained: runnable code
(Python/C++) plus concise notes.

| # | Directory | Topic |
|:--|:---|:---|
| 1 | `01_cpp20_big_four/` | C++20 concepts, ranges, coroutines and modules |
| 12 | `12_stl_under_the_hood/` | STL containers, iterators and algorithms internals |
| 13 | `13_smart_pointers/` | `unique_ptr`, `shared_ptr`, `weak_ptr` |
| 14 | `14_reinventing_the_wheel/` | Custom Vector, UniquePtr, SharedPtr, String, Optional |
| 15 | `15_networking_edge_core/` | Internet edge and core, delay, layering, security |
| 16 | `16_networking_application/` | Application layer: HTTP, DNS, email, P2P, CDNs, sockets |
| 17 | `17_networking_transport/` | Transport layer: UDP, reliable transfer, TCP, congestion, QUIC |
| 18 | `18_networking_data_plane/` | Network layer data plane: routers, IPv4, NAT, SDN |
| 19 | `19_networking_control_plane/` | Control plane: Dijkstra, OSPF, BGP, ICMP, SDN controllers |
| 20 | `20_os_cpu_virtualization/` | Processes, the process API, limited direct execution |
| 21 | `21_os_scheduling/` | FIFO, SJF, STCF, round-robin, MLFQ, lottery, multi-CPU |
| 22 | `22_os_memory_virtualization/` | Address spaces, base/bounds, segmentation |
| 23 | `23_os_free_space/` | Free lists, first/best/worst fit, buddy, slab |
| 24 | `24_os_paging/` | Paging, page tables, TLBs, multi-level page tables |
| 25 | `25_os_swapping/` | Swapping and page replacement (OPT, FIFO, LRU, clock, Belady) |
| 26 | `26_os_threads/` | Threads, the thread API, race conditions |
| 27 | `27_os_locks/` | Spinlocks, test-and-set, CAS, ticket and queue locks |
| 28 | `28_os_locked_data_structures/` | Locked/approximate counters, lists, queues, hash tables |
| 29 | `29_os_condition_variables/` | Condition variables, semaphores, producer/consumer |
| 30 | `30_os_concurrency_bugs/` | Concurrency bugs, deadlock conditions, prevention |
| 31 | `31_os_event_concurrency/` | Event-based concurrency and event loops |

## Verify

```bash
# Every Python example is runnable with self-checks.
for f in $(find . -name '*.py'); do python3 "$f"; done

# C++ deep dives
g++ -std=c++20 -fcoroutines 01_cpp20_big_four/ranges_pipeline.cpp -o /tmp/r && /tmp/r
g++ -std=c++20 14_reinventing_the_wheel/test_suite.cpp -o /tmp/wheel && /tmp/wheel
g++ -std=c++20 -fmodules-ts -x c++ -c 01_cpp20_big_four/modules/math.ixx -o /tmp/math.o
```

Or run `make test-interview` from the repository root, which executes every
Python self-check and the C++ suites.
