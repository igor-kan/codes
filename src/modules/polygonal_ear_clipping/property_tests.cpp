#include "interface.hpp"
#include <cassert>
#include <cmath>

int main() {
    using namespace codes_polygonal_ear_clipping;
    auto chks = parallel_checksum_batches({{1, 2, 3}, {4, 5, 6}});
    assert(chks.size() == 2 && chks[0] != chks[1]);
    std::vector<Vec2> sq = {{0,0},{2,0},{2,2},{0,2}};
    assert(ear_clip_triangulate(sq).size() == 2);
    return 0;
}
