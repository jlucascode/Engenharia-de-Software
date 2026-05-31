#include <stdio.h>

void converter(float celsius, float *fahrenheit) {
    *fahrenheit = (celsius * 9.0 / 5.0) + 32.0;
}

int main() {
    float c, f;
    printf("Digite a temperatura em Celsius: ");
    scanf("%f", &c);
    converter(c, &f);
    printf("%.2f°C = %.2f°F\n", c, f);
    return 0;
}
