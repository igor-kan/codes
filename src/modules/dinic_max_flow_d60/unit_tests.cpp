#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_dinic_max_flow_d60;
    validate_problem_size(1);
    DinicFlow df(6);
    df.add_edge(0, 1, 16); df.add_edge(0, 2, 13);
    df.add_edge(1, 2, 10); df.add_edge(1, 3, 12);
    df.add_edge(2, 1, 4);  df.add_edge(2, 4, 14);
    df.add_edge(3, 2, 9);  df.add_edge(3, 5, 20);
    df.add_edge(4, 3, 7);  df.add_edge(4, 5, 4);
    assert(df.max_flow(0, 5) == 23);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
