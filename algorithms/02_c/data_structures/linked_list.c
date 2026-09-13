#include <stdlib.h>
#include <stdio.h>
typedef struct Node { int data; struct Node *next; } Node;
Node *push(Node *head, int val){ Node *n=malloc(sizeof(Node)); n->data=val; n->next=head; return n; }
void print_list(Node *h){ while(h){ printf("%d->",h->data); h=h->next; } printf("NULL\n"); }
