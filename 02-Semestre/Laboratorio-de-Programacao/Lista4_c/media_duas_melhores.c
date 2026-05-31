#include <stdio.h>

int main() {
    float n1, n2, n3, menor, media;

    printf("Digite as 3 notas: ");
    scanf("%f %f %f", &n1, &n2, &n3);

    menor = n1;
    if (n2 < menor) menor = n2;
    if (n3 < menor) menor = n3;

    media = (n1 + n2 + n3 - menor) / 2.0;

    printf("Media com as 2 notas mais altas: %.2f\n", media);
    return 0;
}
