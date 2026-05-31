#include <stdio.h>
#include <stdlib.h>

typedef struct ImoveisDaRua {
    char *complemento;
    char imovelComercial;
    int numero;
    struct ImoveisDaRua *prox;
} IDR;

int main() {
    // Alocação
    IDR *casa342 = malloc(sizeof(IDR));
    IDR *apartamento17 = malloc(sizeof(IDR));
    IDR *mercantill = malloc(sizeof(IDR));


    mercantill->numero = 1;
    mercantill->complemento = "Casa Comercial, 521 m2";
    mercantill->imovelComercial = 'S';


    apartamento17->numero = 17;
    apartamento17->imovelComercial = 'N';
    apartamento17->complemento = "Predio, 4 Andares, 182 m2";

    casa342->numero = 342;
    casa342->complemento = "Casa, 284 m2";
    casa342->imovelComercial = 'N';

    // Encadeamento (Casa -> Apartamento -> Mercantil -> Fim)
    casa342->prox = apartamento17;
    apartamento17->prox = mercantill;
    mercantill->prox = NULL;

    return 0;
}