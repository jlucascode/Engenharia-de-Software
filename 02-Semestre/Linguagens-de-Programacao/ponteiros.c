#include <stdio.h>
#include <stdlib.h>

void display(int var, int *ptr);
void update(int *ptr);
int main() {

    int var = 15;
    int *ptr;
    ptr = &var; // ptr aponta para o endereço de var
    display(var, ptr);
    update(&var); // Passando o endereço de var para a função update
    //*ptr = 70; // Modificando o valor de var através do ponteiro
    //ptr = &var;

    display(var, ptr);
    // printf("Valor de var: %d\n", var);
    // printf("Endereco de var: %p\n", &var);
    // printf("Conteudo apontado por ptr: %d\n", *ptr);
    // printf("Endereco armazenado em ptr: %p\n", ptr);
    // printf("Endereco de ptr: %p\n", &ptr);
    
    // *ptr = 20; // Modificando o valor de var através do ponteiro
    // printf("\n\n");
    // printf("Valor de var: %d\n", var);
    // printf("Endereco de var: %p\n", &var);
    // printf("Conteudo apontado por ptr: %d\n", *ptr);
    // printf("Endereco armazenado em ptr: %p\n", ptr);
    // printf("Endereco de ptr: %p\n", &ptr);
    
    printf("Fim do programa.\n\n");
    return 0;
}
void display(int var, int *ptr) {
    printf("\n\n");
    printf("Valor de var: %d\n", var);
    printf("Endereco de var: %p\n", &var);
    printf("Conteudo apontado por ptr: %d\n", *ptr);
    printf("Endereco armazenado em ptr: %p\n", ptr);
    printf("Endereco de ptr: %p\n", &ptr);
}
void update(int *p) {
    *p = *p + 1; // Incrementa o valor apontado por p (que é var) em 1
}
// *ptr : o apontado por, conteudo do endereço da variavel var que ptr aponta, ou seja, o valor de var
//  ptr: o endereço da variavel
//  &ptr: o endereço do ponteiro