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
                NO* aux = inicio;
                for(int i=0; i<tam -1; i++){
                    aux = aux->prox;
                }
                aux->prox = novo;
                tam++;
            }else{
                //meio ...
                NO* aux = inicio;
                for(int i=0; i<pos -1; i++){
                    aux = aux->prox;
                }
                novo->prox = aux->prox;
                aux->prox = novo;
                tam++;
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

void pokemon_maior_nivel(){
    //percorrer a lista procurando o pokemon de maior nivel
    //imprimir os dados do pokemon
}


int main() {
  
    add("Pikachu", 18, "eletrico", 'm', 18271, 0);

    add("Raichu", 150, "eletrico", 'm', 18272, 0);

    add("Pichu", 5, "eletrico", 'f', 18273, 0);

    add("Bulbassaur", 151, "planta", 'f', 18274, 3);

    add("Clafairy", 27, "fada", 'm', 18275, 2);

    add("Arceus", 200, "normal", 'f', 18276, 4);

    add("Vaporeon", 300, "agua", 'f', 18277, 6);

    imprimir();

 return 0;
}
