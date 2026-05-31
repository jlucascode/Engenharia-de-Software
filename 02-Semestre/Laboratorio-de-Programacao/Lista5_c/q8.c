#include <stdio.h>

int main() {
    printf("Tabela ASCII (0 a 127)\n");
    printf("Dec  Hex  Caractere\n");
    printf("-------------------\n");

    for (int i = 0; i <= 127; i++) {
        if (i >= 32 && i <= 126)
            printf("%3d  %2x   %c\n", i, i, i);
        else if (i == 0)
            printf("%3d  %2x   NUL\n", i, i);
        else if (i == 7)
            printf("%3d  %2x   BEL\n", i, i);
        else if (i == 8)
            printf("%3d  %2x   BS\n", i, i);
        else if (i == 9)
            printf("%3d  %2x   TAB\n", i, i);
        else if (i == 10)
            printf("%3d  %2x   LF\n", i, i);
        else if (i == 13)
            printf("%3d  %2x   CR\n", i, i);
        else if (i == 27)
            printf("%3d  %2x   ESC\n", i, i);
        else if (i == 127)
            printf("%3d  %2x   DEL\n", i, i);
        else
            printf("%3d  %2x   (controle)\n", i, i);
    }

    return 0;
}
