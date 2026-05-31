#include <stdio.h>

// Ponteiro para funcao: uma variavel que armazena o endereco de uma funcao,
// permitindo chama-la indiretamente. Util para callbacks, tabelas de funcoes
// e polimorfismo.

// Referencias:
// - https://en.cppreference.com/w/c/language/pointer
// - https://www.geeksforgeeks.org/function-pointer-in-c/

// Funcoes de exemplo
int soma(int a, int b) {
    return a + b;
}

int subtrai(int a, int b) {
    return a - b;
}

int multiplica(int a, int b) {
    return a * b;
}

int main() {
    // Declaracao de um ponteiro para funcao que recebe dois ints e retorna int
    int (*op)(int, int);

    int x = 10, y = 3;

    // Aponta para a funcao soma
    op = soma;
    printf("soma(%d, %d) = %d\n", x, y, op(x, y));

    // Aponta para a funcao subtrai
    op = subtrai;
    printf("subtrai(%d, %d) = %d\n", x, y, op(x, y));

    // Aponta para a funcao multiplica
    op = multiplica;
    printf("multiplica(%d, %d) = %d\n", x, y, op(x, y));

    // Tabela de funcoes (array de ponteiros para funcao)
    int (*ops[3])(int, int) = {soma, subtrai, multiplica};
    char *nomes[3] = {"soma", "subtrai", "multiplica"};

    printf("\nUsando tabela de funcoes:\n");
    for (int i = 0; i < 3; i++) {
        printf("%s(%d, %d) = %d\n", nomes[i], x, y, ops[i](x, y));
    }

    return 0;
}
