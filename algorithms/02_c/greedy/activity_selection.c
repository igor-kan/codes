/* Activity-selection problem (CLRS 16.1). */
#include <assert.h>
#include <stdio.h>
#include <stdlib.h>

typedef struct { int start, finish; } Activity;

static int cmp(const void *x, const void *y) {
    const Activity *a = x, *b = y;
    return (a->finish > b->finish) - (a->finish < b->finish);
}

int main(void) {
    Activity acts[] = {{1,4},{3,5},{0,6},{5,7},{3,9},{5,9},{6,10},{8,11},{8,12},{2,14},{12,16}};
    int n = sizeof(acts) / sizeof(acts[0]);
    qsort(acts, n, sizeof(Activity), cmp);
    int count = 0, last = -1;
    for (int i = 0; i < n; ++i)
        if (acts[i].start >= last) { count++; last = acts[i].finish; }
    assert(count == 4);
    printf("activity selection ok\n");
    return 0;
}
