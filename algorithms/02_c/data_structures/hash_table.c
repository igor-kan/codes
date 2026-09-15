/* Separate-chaining hash table. */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUCKETS 16
typedef struct Entry { char *key; int value; struct Entry *next; } Entry;

static Entry *table[BUCKETS];

static unsigned hash(const char *key) {
    unsigned h = 5381;
    while (*key) h = h * 33 + (unsigned char)*key++;
    return h % BUCKETS;
}

void put(const char *key, int value) {
    unsigned index = hash(key);
    for (Entry *e = table[index]; e; e = e->next)
        if (!strcmp(e->key, key)) { e->value = value; return; }
    Entry *e = malloc(sizeof(Entry));
    e->key = strdup(key);
    e->value = value;
    e->next = table[index];
    table[index] = e;
}

int get(const char *key, int *out) {
    for (Entry *e = table[hash(key)]; e; e = e->next)
        if (!strcmp(e->key, key)) { *out = e->value; return 1; }
    return 0;
}

int main(void) {
    put("one", 1);
    put("two", 2);
    int value = 0;
    if (!get("two", &value) || value != 2) return 1;
    if (get("three", &value)) return 1;
    printf("hash table ok\n");
    return 0;
}
