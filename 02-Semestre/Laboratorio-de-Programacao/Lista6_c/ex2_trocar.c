#include <stdio.h>

void trocar(int *a, int *b) {
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main() {
    int x, y;
    printf("Digite dois numeros inteiros: ");
    scanf("%d %d", &x, &y);
    trocar(&x, &y);
    printf("Apos troca: x = %d, y = %d\n", x, y);
    return 0;
}
