
#include <stdio.h>
int main() {
    char nome[100];
    int dia, mes, ano;
    printf("Digite seu nome completo:\n ");
    scanf(" %[^\n]", nome);
    printf("Digite sua data de nascimento:\n ");
    scanf("%d/%d/%d", &dia, &mes, &ano);
    printf("%s, %d/%d/%d\n", nome, dia, mes, ano);
    return 0;
}
