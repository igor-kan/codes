#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_matrix_path_count_d59;
    validate_problem_size(1);
    std::vector<std::vector<long long>> cyc = {{0,1,0},{0,0,1},{1,0,0}};
    auto r = count_k_walks(cyc, 6);
    assert(r[0][0] == 1 && r[0][1] == 0);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
