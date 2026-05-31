#include <stdio.h>

void trocar(int *a, int *b) {
    int aux; // Variável auxiliar para não perder o valor durante a troca

    aux = *a;  
    *a = *b;   
    *b = aux;
}

int main() {
    int x = 10;
    int y = 20;

    printf("Antes da troca: x = %d, y = %d\n", x, y);

    trocar(&x, &y);

    printf("Depois da troca: x = %d, y = %d\n", x, y);

    return 0;
}
