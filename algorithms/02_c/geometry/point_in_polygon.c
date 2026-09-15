/* Ray-casting point-in-polygon test. */
#include <stdio.h>
#include <stdbool.h>
int main(void) {
    double px = 2, py = 2;
    double xs[] = {0, 4, 4, 0}, ys[] = {0, 0, 4, 4};
    bool inside = false;
    int n = 4;
    for (int i = 0, j = n - 1; i < n; j = i++) {
        if (((ys[i] > py) != (ys[j] > py)) &&
            (px < (xs[j] - xs[i]) * (py - ys[i]) / (ys[j] - ys[i]) + xs[i]))
            inside = !inside;
    }
    if (!inside) return 1;
    printf("point in polygon ok\n");
    return 0;
}
