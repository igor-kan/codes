#include <stdio.h>
#include <assert.h>
#include "levenshtein_distance.h"

int main(void) {
    assert(levenshtein("kitten", "sitting") == 3);
    assert(levenshtein("flaw", "lawn") == 2);
    printf("test_levenshtein_distance PASSED\n");
    return 0;
}
