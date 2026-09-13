#include <stdio.h>
#define MAX 1000
typedef struct { int data[MAX]; int head,tail,size; } Queue;
void enqueue(Queue *q,int v){ q->data[q->tail]=(q->tail+1)%MAX; q->size++; }
int  dequeue(Queue *q){ int v=q->data[q->head]; q->head=(q->head+1)%MAX; q->size--; return v; }
