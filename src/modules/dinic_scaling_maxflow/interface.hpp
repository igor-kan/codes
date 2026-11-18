#pragma once
#include "types.hpp"
#include "errors.hpp"

namespace codes_dinic_scaling_maxflow {
class ScalingDinic {
public:
    explicit ScalingDinic(int n);
    void add_edge(int u, int v, std::int64_t cap);
    std::int64_t max_flow(int s, int t);
private:
    int n_;
    std::vector<std::vector<FlowEdge>> adj_;
    std::vector<int> level_;
    std::vector<std::size_t> ptr_;
    bool bfs(int s, int t, std::int64_t delta);
    std::int64_t dfs(int u, int t, std::int64_t pushed, std::int64_t delta);
};

void validate_problem_size(int n);
std::int64_t fast_checksum_span(const std::vector<std::int64_t>& xs);
std::vector<std::int64_t> parallel_checksum_batches(const std::vector<std::vector<std::int64_t>>& batches);
void verify_module_postcondition(bool ok, const char* msg);
} // namespace codes_dinic_scaling_maxflow
