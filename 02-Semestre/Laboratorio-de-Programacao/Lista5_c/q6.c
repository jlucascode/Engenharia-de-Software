#include <stdio.h>

int main() {
    int a = 5;
    int *p;
    p = &a;

    // A variavel p armazena:
    // a) O valor de a      -> INCORRETO (p armazena o endereco, nao o valor 5)
    // b) O endereco de a   -> CORRETO  (p = &a, guarda o endereco de a)
    // c) O tamanho de a    -> INCORRETO (sizeof diz o tamanho)
    // d) O tipo de a       -> INCORRETO (o tipo e definido na declaracao)

    printf("Resposta: b) O endereco de a\n");
    printf("p = %p, &a = %p\n", (void*)p, (void*)&a);

    return 0;
}
