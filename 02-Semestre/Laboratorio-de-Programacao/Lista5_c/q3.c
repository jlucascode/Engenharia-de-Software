#include <stdio.h>

int main() {
    int a, b;
    int *p, *q;

    p = &a;
    q = &b;

    printf("Endereco de a (p): %p\n", (void*)p);
    printf("Endereco de b (q): %p\n", (void*)q);

    if (p > q)
        printf("Maior endereco: p (%p)\n", (void*)p);
    else if (q > p)
        printf("Maior endereco: q (%p)\n", (void*)q);
    else
        printf("Os enderecos sao iguais.\n");

    return 0;
}
