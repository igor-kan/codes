#include "convex_hull_graham.h"
#include <stdlib.h>

static Point2D p0;

static double cross_product(Point2D a, Point2D b, Point2D c) {
    return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}

static int compare_points(const void *vp1, const void *vp2) {
    Point2D *p1 = (Point2D *)vp1;
    Point2D *p2 = (Point2D *)vp2;
    double cp = cross_product(p0, *p1, *p2);
    if (cp == 0) return 0;
    return (cp > 0) ? -1 : 1;
}

int convex_hull_graham(Point2D *pts, int n, Point2D *hull) {
    if (n < 3) return 0;
    
    // Find bottom-most point
    int min_idx = 0;
    for (int i = 1; i < n; ++i) {
        if (pts[i].y < pts[min_idx].y || (pts[i].y == pts[min_idx].y && pts[i].x < pts[min_idx].x)) {
            min_idx = i;
        }
    }
    Point2D temp = pts[0]; pts[0] = pts[min_idx]; pts[min_idx] = temp;
    p0 = pts[0];
    
    qsort(&pts[1], n - 1, sizeof(Point2D), compare_points);
    
    hull[0] = pts[0];
    hull[1] = pts[1];
    hull[2] = pts[2];
    int h_size = 3;
    
    for (int i = 3; i < n; ++i) {
        while (h_size >= 2 && cross_product(hull[h_size - 2], hull[h_size - 1], pts[i]) <= 0) {
            h_size--;
        }
        hull[h_size++] = pts[i];
    }
    return h_size;
}
