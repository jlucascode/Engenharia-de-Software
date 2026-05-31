#include <stdio.h>

void dobrar(int *num) {
    *num *= 2; // Multiplica o valor apontado por 2
}

int main(){
   int num;
    printf("Digite um numero inteiro: ");
    scanf("%d", &num);

    dobrar(&num);
    printf("O dobro do numero eh: %d", num);
    return 0;
}
/*Dado um número inteiro informado pelo usuário, desenvolva uma função
chamada dobrar capaz de alterar o valor original da variável para o dobro
utilizando ponteiros. Ao final, exiba o valor atualizado na função principal. */