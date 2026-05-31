#include <stdio.h>

int main() {
    int opcao;
    float temp, convertida;

    printf("Conversor de Temperatura\n");
    printf("1 - Celsius para Farenheit\n");
    printf("2 - Farenheit para Celsius\n");
    printf("Escolha: ");
    scanf("%d", &opcao);

    switch (opcao) {
        case 1:
            printf("Digite a temperatura em Celsius: ");
            scanf("%f", &temp);
            convertida = (9.0 * temp / 5.0) + 32.0;
            printf("%.2f C = %.2f F\n", temp, convertida);
            break;
        case 2:
            printf("Digite a temperatura em Farenheit: ");
            scanf("%f", &temp);
            convertida = 5.0 * (temp - 32.0) / 9.0;
            printf("%.2f F = %.2f C\n", temp, convertida);
            break;
        default:
            printf("Opcao invalida\n");
    }

    return 0;
}
