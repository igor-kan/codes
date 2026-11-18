#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_polygonal_ear_clipping;
    validate_problem_size(1);
    std::vector<Vec2> p = {{0,0},{4,0},{4,3},{2,1.5},{0,3}};
    auto tris = ear_clip_triangulate(p);
    assert(tris.size() == 3);
    double sum2 = 0.0;
    for (auto t : tris) sum2 += polygon_signed_area2({p[t.a], p[t.b], p[t.c]});
    assert(std::fabs(sum2 - polygon_signed_area2(p)) < 1e-9);
    verify_module_postcondition(true, "unit ok");
    return 0;
}
