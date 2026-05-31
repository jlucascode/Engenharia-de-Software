#include <stdio.h>

int ehPrimo(int n) {
    int i;
    if (n < 2) return 0;
    for (i = 2; i * i <= n; i++) {
        if (n % i == 0) return 0;
    }
    return 1;
}

int main() {
    int i;
    printf("Numeros primos ate 1000:\n");
    for (i = 2; i <= 1000; i++) {
        if (ehPrimo(i))
            printf("%d ", i);
    }
    printf("\n");
    return 0;
}
