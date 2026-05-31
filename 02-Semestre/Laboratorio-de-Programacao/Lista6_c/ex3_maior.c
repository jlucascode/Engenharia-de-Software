#include <stdio.h>

int maior(int *a, int *b) {
    return (*a > *b) ? *a : *b; //operador ternário compara os valores apontados por a e b e retorna o maior deles
}

int main() {
    int x, y;
    printf("Digite dois numeros inteiros: ");
    scanf("%d %d", &x, &y);
    printf("O maior valor eh: %d\n", maior(&x, &y));
    return 0;
}
