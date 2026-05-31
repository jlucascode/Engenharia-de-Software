#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>

static int eh_consoante(char c) {
    if (!isalpha((unsigned char)c))
        return 0;

    char lower = tolower((unsigned char)c);
    return lower != 'a' && lower != 'e' && lower != 'i' && lower != 'o' && lower != 'u';
}

void cripto(const char *senha) {
    char pilha[1024];
    int topo = 0;

    for (size_t i = 0; senha[i] != '\0'; i++) {
        char c = senha[i];

        if (eh_consoante(c)) {
            pilha[topo++] = c;
        } else {
            while (topo > 0)
                putchar(pilha[--topo]);
            putchar(c);
        }
    }

    while (topo > 0)
        putchar(pilha[--topo]);
}

int main(void) {
    char entrada[1024];

    if (fgets(entrada, sizeof(entrada), stdin) == NULL)
        return EXIT_FAILURE;

    size_t len = strlen(entrada);
    if (len > 0 && entrada[len - 1] == '\n')
        entrada[len - 1] = '\0';

    cripto(entrada);
    putchar('\n');

    return EXIT_SUCCESS;
}