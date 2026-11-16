#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_bridges_articulation_lowlink {
CutReport find_bridges_and_articulations(std::size_t n, const std::vector<UndirectedEdge>& edges);
Status validate_graph(std::size_t n, const std::vector<UndirectedEdge>& edges);
CutReport find_bridges_iterative(std::size_t n, const std::vector<UndirectedEdge>& edges);
std::vector<CutReport> batch_cut_reports(const std::vector<std::pair<std::size_t, std::vector<UndirectedEdge>>>& graphs);
Status verify_cut_oracle(std::size_t n, const std::vector<UndirectedEdge>& edges, const CutReport& rep);
} // namespace codes_bridges_articulation_lowlink
