#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_li_chao_segment_d60;
    validate_problem_size(1);
    LiChaoTree lc(0, 64);
    lc.add_line(2, 10);
    lc.add_line(-1, 25);
    lc.add_line(0, 18);
    assert(lc.min_at(0) == 10);
    assert(lc.min_at(5) == 18);
    assert(lc.min_at(10) == 15);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
