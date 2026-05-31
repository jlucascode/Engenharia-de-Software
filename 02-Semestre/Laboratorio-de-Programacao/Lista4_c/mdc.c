#include <stdio.h>

int mdc(int a, int b) {
    int resto;
    while (b != 0) {
        resto = a % b;
        a = b;
        b = resto;
    }
    return a;
}

int main() {
    int n1, n2;
    printf("Digite dois inteiros: ");
    scanf("%d %d", &n1, &n2);
    printf("MDC(%d, %d) = %d\n", n1, n2, mdc(n1, n2));
    return 0;
}
