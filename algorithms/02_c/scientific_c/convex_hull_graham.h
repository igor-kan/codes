#ifndef CONVEX_HULL_GRAHAM_H
#define CONVEX_HULL_GRAHAM_H

typedef struct {
    double x, y;
} Point2D;

int convex_hull_graham(Point2D *pts, int n, Point2D *hull);

#endif
