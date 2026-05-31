#include <stdio.h>
int main() {
    float reais, cotacao;
    printf("Valor em R$ e Cotacao do US$: ");
    scanf("%f %f", &reais, &cotacao);
    printf("Voce tem: US$ %.2f", reais / cotacao);
    return 0;
}