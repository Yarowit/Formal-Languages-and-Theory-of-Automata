#include <stdio.h>
#include <stdlib.h>

struct stack
{
    int v;
    struct stack* next;
};

struct stack* nStack(int v){
    struct stack* n = (struct stack*) malloc(sizeof(struct stack));
    n->next = NULL;
    n->v = v;
    return n;
}

struct stack* push(struct stack* top, int v){
    struct stack* n = (struct stack*) malloc(sizeof(struct stack));
    n->next = top;
    n->v = v;
    return n;
}

struct stack* pop(struct stack* top){
    struct stack* n = top->next;
    top->next = NULL;
    free(top);
    return n;
}

struct stack* reset(struct stack* s){
    while(s)
        s=pop(s);
    return s;
}