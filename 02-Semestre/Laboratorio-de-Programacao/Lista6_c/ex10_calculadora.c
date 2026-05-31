#include <stdio.h>

float somar(float a, float b) { return a + b; }
float subtrair(float a, float b) { return a - b; }
float multiplicar(float a, float b) { return a * b; }
float dividir(float a, float b) { return a / b; }

int main() {
    float x, y;
    char op;
    float (*operacao)(float, float);

    printf("Digite dois numeros reais: ");
    scanf("%f %f", &x, &y);
    printf("Digite a operacao (+, -, *, /): ");
    scanf(" %c", &op);

    switch (op) {
        case '+': operacao = somar; break;
        case '-': operacao = subtrair; break;
        case '*': operacao = multiplicar; break;
        case '/': operacao = dividir; break;
        default:
            printf("Operacao invalida\n");
            return 1;
    }

    printf("Resultado: %.2f\n", operacao(x, y));
    return 0;
}
