#include <stdlib.h>
#include <stdio.h>

typedef struct NO{

    //dados da aplicacao
    char * nome_livro;
    char* autor;
    int isbn;
    char* genero;
    float preco;

    //mecanismo de uniao de nos
    struct NO * prox;
    struct NO *ant;

}NO;

NO *inicio = NULL;
NO *fim = NULL;
int tam = 0;

void add(char * nome_livro, char* autor, int isbn, char* genero, float preco, int pos){
   
    if(pos >= 0 && pos <= tam){

        NO * novo = malloc(sizeof(NO));
        novo->nome_livro = nome_livro;
        novo->autor = autor;
        novo->isbn = isbn;
        novo->genero = genero;
        novo->preco = preco;
        novo->prox = NULL;
        novo->ant = NULL;

        //tratar como inserir 

        if(inicio == NULL){ //lista vazia
            //operacao de encaixe
            inicio = novo;
            fim = novo;
            tam++;
        }else{ // lista nao esta vazia...

            if(pos == 0){ // caso do inicio

                novo->prox = inicio;
                inicio->ant = novo;
                inicio = novo;
                tam++;

            }else if(pos == tam){ //caso do fim
                fim->prox = novo;
                novo->ant = fim;
                fim = novo;
                tam++;
            }else{
                //meio ...
                NO* aux = inicio;
                for(int i=0; i<pos -1; i++){
                    aux = aux->prox;
                }
                novo->prox =aux->prox;
                novo->ant = aux;
                aux->prox->ant = novo;
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
        printf("Nome do livro: %s \n", aux->nome_livro);
        //... fazer os demais dados
        aux = aux->prox;
    }
}

void remover(int pos){

    if(pos >= 0 && pos < tam){

        if(pos == 0){ //inicio
            NO *lixo = inicio;
            inicio = inicio->prox;
            inicio->ant = NULL;
            if(tam == 1){
               fim = NULL;
            }
            free(lixo);
            tam--;
        }else if(pos == tam-1){ // fim
            NO *lixo = fim;
            fim->ant->prox = NULL;
            fim = fim->ant;
            free(lixo);
            tam--;
        }else{
            //meio....
            NO *aux = inicio;
            for(int i= 0; i< pos; i++){
                aux = aux->prox;
            } 
            aux->ant->prox = aux->prox;
            aux->prox->ant = aux->ant; 

            free(aux);
            tam--;
        }
    }

}

int main() {
  
    add("Devoradores de Estrelas", "Andy Weir", 817813, "ficcao", 50.0, 0);

    add("Revolucao dos Bichos", "George W.", 183749, "ficcao", 20.0, 1);

    add("Cartas de amor aos mortos", "Ava Dell", 39334, "juvenil", 40.0, 1);

    add("O Principie", "Maquiavel", 283781, "Romance", 100.0, 3);

    imprimir();

 return 0;
}
