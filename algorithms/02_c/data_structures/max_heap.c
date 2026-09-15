/* Binary max-heap. */
#include <stdio.h>
#define MAX 128
static int h[MAX];
static int n = 0;
static void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }
void push(int v) {
    h[n] = v;
    int i = n++;
    while (i > 0 && h[(i - 1) / 2] < h[i]) { swap(&h[i], &h[(i - 1) / 2]); i = (i - 1) / 2; }
}
int pop(void) {
    int top = h[0];
    h[0] = h[--n];
    int i = 0;
    while (1) {
        int l = 2 * i + 1, r = 2 * i + 2, b = i;
        if (l < n && h[l] > h[b]) b = l;
        if (r < n && h[r] > h[b]) b = r;
        if (b == i) break;
        swap(&h[i], &h[b]);
        i = b;
    }
    return top;
}
int main(void) {
    int v[] = {5, 3, 8, 1, 4};
    for (int i = 0; i < 5; i++) push(v[i]);
    int prev = 1 << 30;
    while (n) { int x = pop(); if (x > prev) return 1; prev = x; }
    printf("max heap ok\n");
    return 0;
}
