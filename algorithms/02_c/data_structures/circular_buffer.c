/* Fixed-size circular buffer. */
#include <stdio.h>
#define CAP 3
static int buf[CAP], head = 0, size = 0;
void cb_push(int v) {
    buf[(head + size) % CAP] = v;
    if (size < CAP) size++; else head = (head + 1) % CAP;
}
int cb_pop(void) {
    int v = buf[head];
    head = (head + 1) % CAP;
    size--;
    return v;
}
int main(void) {
    for (int i = 1; i <= 4; i++) cb_push(i);
    if (cb_pop() != 2 || cb_pop() != 3 || cb_pop() != 4) return 1;
    printf("circular buffer ok\n");
    return 0;
}
