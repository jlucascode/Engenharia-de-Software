#include <stdio.h>

int main() {
    int i = 5, *p;
    p = &i;

    printf("%x %d %d %d %d", p,*p+2,**&p,3**p,**&p+4);
    // Analise:
    // p      -> endereco de i (hexadecimal)
    // *p+2   -> valor de i (5) + 2 = 7
    // **&p   -> *(&p) = p, *p = i = 5
    // 3**p   -> 3 * (*p) = 3 * 5 = 15
    // **&p+4 -> 5 + 4 = 9
    //
    // Saida esperada (exemplo): endereco 7 5 15 9

    return 0;
}
