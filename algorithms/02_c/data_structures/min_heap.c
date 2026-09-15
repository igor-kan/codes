/* Binary min-heap. */
#include <stdio.h>
#include <stdlib.h>

#define MAX 128
static int heap[MAX];
static int size = 0;

static void swap(int *a, int *b) { int t = *a; *a = *b; *b = t; }

void push(int value) {
    heap[size] = value;
    int i = size++;
    while (i > 0 && heap[(i - 1) / 2] > heap[i]) {
        swap(&heap[i], &heap[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}

int pop(void) {
    int root = heap[0];
    heap[0] = heap[--size];
    int i = 0;
    while (1) {
        int smallest = i, left = 2 * i + 1, right = 2 * i + 2;
        if (left < size && heap[left] < heap[smallest]) smallest = left;
        if (right < size && heap[right] < heap[smallest]) smallest = right;
        if (smallest == i) break;
        swap(&heap[i], &heap[smallest]);
        i = smallest;
    }
    return root;
}

int main(void) {
    int values[] = {5, 3, 8, 1, 4};
    for (int i = 0; i < 5; i++) push(values[i]);
    int previous = -1;
    while (size > 0) {
        int value = pop();
        if (value < previous) return 1;
        previous = value;
    }
    printf("min heap ok\n");
    return 0;
}
