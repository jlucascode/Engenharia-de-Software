#include <stdio.h>
#include <stdlib.h>

typedef struct ImoveisDaRua{
    char * complemento;
    char imovelComercial;
    struct ImoveisDaRua *prox;
    int numero;
}IDR;

int main() {
  
    IDR * mercantil1 = malloc(sizeof(IDR));
    IDR * apartamento17 = malloc(sizeof(IDR));
    IDR * casa342 = malloc(sizeof(IDR));
    casa342->imovelComercial = 'N';
    mercantil1->numero = 1;
    mercantil1->complemento = "Casa ...";
    apartamento17->imovelComercial = 'N';
    casa342->numero = 342;
    apartamento17->numero = 17;
    apartamento17->complemento = "Predio ...";
    mercantil1->imovelComercial = 'S';
    casa342->complemento = "Casa ...";

    casa342->prox = apartamento17;
    apartamento17->prox = mercantil1;
    mercantil1->prox = NULL;

    IDR *aux = casa342;
    while(aux != NULL){
        printf("\n --- DADOS DO IMOVEL ---\n");
        printf("Numero: %d\n", aux->numero);
        printf("Complemento: %s\n", aux->complemento);
        printf("O imovel e comercial - S ou residencial - N: %c\n", aux->imovelComercial);
        // aux sai de um no e ir para o proximo!
        //COMO EU FACO ISSO!
        aux = aux->prox;
    
    }


    return 0;
} 