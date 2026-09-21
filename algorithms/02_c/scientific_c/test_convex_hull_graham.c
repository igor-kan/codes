#include <stdio.h>
#include <assert.h>
#include "convex_hull_graham.h"

int main(void) {
    Point2D pts[5] = {
        {0.0, 0.0},
        {1.0, 0.0},
        {1.0, 1.0},
        {0.0, 1.0},
        {0.5, 0.5} // Interior point
    };
    Point2D hull[5];
    int h_len = convex_hull_graham(pts, 5, hull);
    assert(h_len == 4);
    printf("test_convex_hull_graham PASSED\n");
    return 0;
}
