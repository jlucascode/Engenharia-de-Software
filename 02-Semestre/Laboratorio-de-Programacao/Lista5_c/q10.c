#include <stdio.h>

int main() {
    printf("Tabela de Tabuada (1 a 9)\n");
    printf("========================\n\n");

    for (int i = 1; i <= 9; i++) {
        printf("Tabuada do %d:\n", i);
        for (int j = 1; j <= 10; j++) {
            printf("%2d x %2d = %3d\n", i, j, i * j);
        }
        printf("\n");
    }

    return 0;
}
