#include <stdlib.h>
#include <stdio.h>

typedef struct NO{

    //dados da aplicacao
    char * nome_pessoa;
    int ticket_ru;

    //mecanismo de uniao de nos
    struct NO * prox;

}NO;

NO *inicio = NULL;
NO *fim = NULL;
int tam = 0;

void add(char *nome_pessoa, int ticket_ru ){

        NO * novo = malloc(sizeof(NO));
        novo->nome_pessoa = nome_pessoa;
        novo->ticket_ru = ticket_ru;
        novo->prox = NULL;

        //tratar como inserir 

        if(inicio == NULL){ //fila vazia
            //operacao de encaixe
            inicio = novo;
            fim = novo;
            tam++;
        }else{ // fila nao esta vazia...
                fim->prox = novo;
                fim = novo;
                tam++;
        }
}

void imprimir(){
    NO * aux = inicio;
    while(aux != NULL){
        printf("Nome do pessoa: %s \n", aux->nome_pessoa);
        //... fazer os demais dados
        aux = aux->prox;
    }
}

void remover(){

        if(tam >  0){ //inicio
            NO *lixo = inicio;
            inicio = inicio->prox;
            if(tam == 1){
               fim = NULL;
            }
            free(lixo);
            tam--;
        }else{
            printf("A fila esta vazia! :D");
        }

}

int main() {
    
    add("Tatiane", 182373);
    add("Dmitri", 28374);
    add("Pedro", 293734);
    add("Davi", 19283);
    imprimir();
 return 0;
}

//FIFO
//(First In, First Out - primeiro a entrar, primeiro a sair)