#include "interface.hpp"
namespace codes_mo_offline_queries {
Status validate_queries(std::size_t n, const std::vector<RangeQuery>& queries) {
    for (const auto& q : queries) {
        if (q.l > q.r || q.r >= n) return Status::OutOfBounds;
    }
    return Status::Ok;
}
} // namespace codes_mo_offline_queries
