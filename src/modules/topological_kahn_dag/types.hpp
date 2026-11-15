#pragma once
#include <cstddef>
#include <cstdint>
#include <vector>
#include <string>
#include <array>
#include <functional>
#include <utility>

namespace codes_topological_kahn_dag {
struct TopoResult {
    bool is_dag = false;
    std::vector<std::size_t> order;
};
} // namespace codes_topological_kahn_dag
