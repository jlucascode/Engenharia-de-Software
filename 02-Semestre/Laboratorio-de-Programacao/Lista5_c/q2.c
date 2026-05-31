#include <stdio.h>

int main() {
    int i = 5, j = 10;
    int *p, *q;
    p = &i;
    q = &j;

    // Considere as expressoes:

    // p == &i; -> compara o valor de p (endereco de i) com o endereco de i
    printf("p == &i: %d\n", p == &i); // 1 (verdadeiro, p aponta para i)

    // *p - *q; -> subtrai os valores apontados: 5 - 10
    printf("*p - *q: %d\n", *p - *q); // -5

    // **&p; -> &p pega o endereco de p, *&p acessa p (que e &i), **&p acessa i
    printf("**&p: %d\n", **&p); // 5

    // 3 - *p/(*q) + 7; -> 3 - 5/10 + 7 = 3 - 0 + 7 (divisao inteira)
    printf("3 - *p/(*q) + 7: %d\n", 3 - *p/(*q) + 7); // 10

    return 0;
}
