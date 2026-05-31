#include <stdio.h>
int main() {
    char nome[30];
    float fixo, vendas, total, comissao;
    printf("Nome, Salario Fixo e Vendas: ");
    scanf("%s %f %f", nome, &fixo, &vendas);
    comissao = vendas * 0.15;
    total = fixo + comissao;
    printf("Salario Total: R$ %.2f\n", total);
    printf("Sobrou apos imposto (8%%): R$ %.2f", total * 0.92); // 100% - 8% = 92%
    return 0;
} 