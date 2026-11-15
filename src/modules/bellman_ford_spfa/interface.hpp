#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_bellman_ford_spfa {
SsspResult solve_bellman_ford(std::size_t n, const std::vector<std::vector<Edge>>& adj, std::size_t src);
SsspResult solve_spfa(std::size_t n, const std::vector<std::vector<Edge>>& adj, std::size_t src);
Status validate_graph(std::size_t n, std::size_t src);
SsspResult solve_spfa_slf(std::size_t n, const std::vector<std::vector<Edge>>& adj, std::size_t src);
std::vector<SsspResult> batch_sources(std::size_t n, const std::vector<std::vector<Edge>>& adj, const std::vector<std::size_t>& srcs);
Status verify_optimality(const std::vector<std::vector<Edge>>& adj, const SsspResult& res);
} // namespace codes_bellman_ford_spfa
