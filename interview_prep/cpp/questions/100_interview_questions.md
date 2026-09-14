# 100 C++ Interview Questions (curated)

## Language fundamentals
1. What is RAII and why is it the backbone of C++ resource management?
2. Difference between `struct` and `class`?
3. Value categories: lvalue, prvalue, xvalue — with examples.
4. What does `const` mean in each position of `const int * const p`?
5. Difference between pointers and references; when to use each?
6. What is the rule of three/five/zero?
7. Copy elision and guaranteed RVO in C++17.
8. `new`/`delete` vs `malloc`/`free`.
9. Placement new and manual destructor calls.
10. What is an object's lifetime; when does UB occur?

## Object model
11. vtable/vptr mechanics and virtual dispatch cost.
12. Why should a polymorphic base have a virtual destructor?
13. Pure virtual functions, abstract classes and interfaces.
14. Multiple inheritance and the diamond problem (virtual inheritance).
15. `override` and `final` — what problems do they prevent?
16. Object slicing: what it is and how to avoid it.
17. Empty base optimization (EBO).
18. `noexcept` semantics and `std::terminate`.
19. What is a trivially copyable type?
20. Standard-layout and `reinterpret_cast` safety.

## Move semantics & value
21. Explain move construction and when the compiler generates it.
22. What is `std::move` actually doing?
23. Perfect forwarding and universal/forwarding references.
24. Reference collapsing rules.
25. Why is a `noexcept` move constructor important for `vector`?

## Templates & generic programming
26. Function template argument deduction rules.
27. Class template argument deduction (CTAD).
28. Variadic templates and fold expressions.
29. SFINAE and `std::enable_if` vs concepts.
30. What is a non-type template parameter?
31. Template specialization vs overloading.
32. CRTP (curiously recurring template pattern).
33. Type traits and `if constexpr`.
34. What problem do concepts solve?

## Smart pointers & memory
35. `unique_ptr` ownership transfer semantics.
36. `shared_ptr` control block and reference counting.
37. `weak_ptr` and breaking cycles.
38. `make_shared` vs `shared_ptr(new T)`.
39. Custom deleters.
40. `enable_shared_from_this`.
41. What is `std::pmr`?
42. Memory leaks, double free and how tooling catches them (ASan/Valgrind).
43. `std::launder` and pointer provenance.
44. Allocator awareness.

## STL containers
45. `vector` growth strategy and amortized complexity.
46. Iterator invalidation rules per container.
47. `map` vs `unordered_map` complexity and ordering.
48. `deque` internals vs `vector`.
49. When is `std::list` the right choice?
50. `std::array` vs C array.
51. `set`/`multiset` and comparators.
52. `string_view` and dangling views.
53. `span` for non-owning views.
54. `std::optional`, `variant`, `any` use cases.
55. `std::tuple` and structured bindings.

## Algorithms & ranges
56. Complexity guarantees of `std::sort`.
57. `stable_sort` vs `sort`.
58. `lower_bound`/`upper_bound` semantics.
59. `std::nth_element` and quickselect.
60. `std::accumulate` vs `reduce`.
61. Ranges and views (`std::views::filter`).
62. Writing a custom iterator.
63. Predicates and comparators: strict weak ordering.
64. `std::transform` and `std::back_inserter`.
65. Parallel algorithms (`std::execution`).

## Concurrency
66. `std::thread` and joining; `std::jthread`.
67. `mutex`, `lock_guard`, `unique_lock`, `scoped_lock`.
68. Deadlock: conditions and prevention.
69. `condition_variable` and spurious wakeups.
70. `atomic` and the C++ memory model.
71. `memory_order` values and their guarantees.
72. Lock-free programming basics; ABA problem.
73. `future`, `promise`, `packaged_task`, `async`.
74. Thread pool design.
75. False sharing and cache-line padding.

## Performance & optimization
76. Copy elision and avoiding needless copies.
77. Small string/small vector optimization.
78. Cache locality and data-oriented design.
79. Branch prediction and `[[likely]]`.
80. Inlining, LTO and PGO.
81. `constexpr` evaluation and compile-time work.
82. RVO/NRVO and return-by-value.
83. Profiling: perf, VTune, gprof.
84. Zero-cost abstractions in C++.
85. Avoiding virtual dispatch via CRTP or variants.

## Modern C++ (C++17/20/23)
86. Structured bindings.
87. `if`/`switch` with initializer.
88. `std::filesystem`.
89. `std::string_view`, `std::span`.
90. `std::chrono` durations and time points.
91. Modules (C++20).
92. Coroutines: `co_await`, `co_return`, `co_yield`.
93. Ranges and concepts (C++20).
94. `constexpr`/`consteval`/`constinit`.
95. `std::bit_cast`, `std::to_address`.
96. `std::mdspan` (C++23).
97. Deducing `this` (C++23).
98. `std::expected` (C++23).
99. `std::print` (C++23).
100. What does "undefined behaviour" mean, and why does it matter?
