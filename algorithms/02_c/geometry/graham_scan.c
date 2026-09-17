#include <stdio.h>
#include <stdlib.h>
#include <assert.h>
typedef struct { int x, y; } Point;
int cross(Point o, Point a, Point b) {
    return (a.x - o.x) * (b.y - o.y) - (a.y - o.y) * (b.x - o.x);
}
int main(void) {
    Point o = {0, 0}, a = {1, 0}, b = {1, 1};
    assert(cross(o, a, b) > 0);
    printf("C Graham Scan primitive verified.\n");
    return 0;
}
