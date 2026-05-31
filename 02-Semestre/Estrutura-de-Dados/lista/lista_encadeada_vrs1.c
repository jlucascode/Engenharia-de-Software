#include <stdlib.h>
#include <stdio.h>

typedef struct NO{

    //dados da aplicacao
    char * nome;
    int nivel;
    char *tipo;
    char genero;
    int pokedex;

    //mecanismo de uniao de nos
    struct NO * prox;

}NO;

NO *inicio = NULL;
int tam = 0;

void add(char *nome, int nivel, char *tipo, char genero, int pokedex, int pos){
   
    if(pos >= 0 && pos <= tam){

        NO * novo = malloc(sizeof(NO));
        novo->nome = nome;
        novo->nivel = nivel;
        novo->tipo = tipo;
        novo->genero = genero;
        novo->pokedex = pokedex;
        novo->prox = NULL;

        //tratar como inserir 

        if(inicio == NULL){ //lista vazia
            //operacao de encaixe
            inicio = novo;
            tam++;
        }else{ // lista nao estar vazia...

            if(pos == 0){ // caso do inicio

                novo->prox = inicio;
                inicio = novo;
                tam++;

            }else if(pos == tam){ //caso do fim
                
            }else{
                //meio ...
            }
        }
    }else{
        printf("Posicao invalida! Isso aqui é uma listaaaaaaaa! :D");
    }

}

void imprimir(){
    NO * aux = inicio;
    while(aux != NULL){
        printf("Nome do pokemon: %s \n", aux->nome);
        //... fazer os demais dados
        aux = aux->prox;
    }
}


int main() {
    add("Pikachu", 18, "eletrico", 'm', 18271, 0);
    add("Raichu", 150, "eletrico", 'm', 18272, 0);
    add("Pichu", 5, "eletrico", 'f', 18273, 0);
    imprimir();

 return 0;
}
