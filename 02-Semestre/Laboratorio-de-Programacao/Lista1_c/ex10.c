#include <stdio.h>
int main() {
    int n;
    printf("Digite um numero: ");
    scanf("%d", &n);
    printf("Hexadecimal: %x\nOctal: %o", n, n); // %x para hexa, %o para octal
    return 0;
}