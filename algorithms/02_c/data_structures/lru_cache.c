/* LRU cache using a small array-based recency list. */
#include <stdio.h>
#include <stdlib.h>

#define CAPACITY 2
typedef struct { int key, value, used; } Slot;

static Slot slots[CAPACITY];
static int clock_tick = 0;

static Slot *find(int key) {
    for (int i = 0; i < CAPACITY; i++)
        if (slots[i].used && slots[i].key == key) return &slots[i];
    return NULL;
}

int get(int key) {
    Slot *slot = find(key);
    if (!slot) return -1;
    slot->used = ++clock_tick;
    return slot->value;
}

void put(int key, int value) {
    Slot *slot = find(key);
    if (slot) { slot->value = value; slot->used = ++clock_tick; return; }
    int victim = 0;
    for (int i = 0; i < CAPACITY; i++)
        if (!slots[i].used) { victim = i; break; }
        else if (slots[i].used < slots[victim].used) victim = i;
    slots[victim] = (Slot){key, value, ++clock_tick};
}

int main(void) {
    put(1, 1);
    put(2, 2);
    if (get(1) != 1) return 1;
    put(3, 3);
    if (get(2) != -1) return 1;
    printf("lru cache ok\n");
    return 0;
}
