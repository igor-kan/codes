#include <stdio.h>
#define MAX 1000
typedef struct { int data[MAX]; int top; } Stack;
void init(Stack *s){ s->top=-1; }
void push(Stack *s, int v){ s->data[++s->top]=v; }
int  pop(Stack *s){ return s->data[s->top--]; }
int  peek(Stack *s){ return s->data[s->top]; }
int  empty(Stack *s){ return s->top==-1; }
