#include <stdlib.h>
#include <stdio.h>

typedef struct NO{

    //dados da aplicacao
    char * nome_produto;
    float preco;
    //mecanismo de uniao de nos
    struct NO * prox;

}NO;

NO *topo = NULL;
int tam = 0;

void add(char *nome_produto, float preco){

        NO * novo = malloc(sizeof(NO));
        novo->nome_produto = nome_produto;
        novo->preco = preco;
        novo->prox = NULL;

        //tratar como inserir 

        if(topo == NULL){ //pilha vazia
            //operacao de encaixe
            topo = novo;
            tam++;
        }else{ // pilha nao esta vazia...

                novo->prox = topo;
                topo = novo;
                tam++;   
        }
}

void imprimir(){
    NO * aux = topo;
    while(aux != NULL){
        printf("Nome do produto: %s \n", aux->nome_produto);
        //... fazer os demais dados
        aux = aux->prox;
    }
}

void remover(){
        if(tam > 0){ //topo
            NO *lixo = topo;
            topo = topo->prox;
            free(lixo);
            tam--;
        }else{
            printf("A pilha esta vazia! :D\n");
        }
}

int main() {

    add("Quilha", 800);

    add("Deck", 120.0);

    add("Deck", 100);

    imprimir();
   
    
 return 0;
}

//LIFO 
//(Last In, First Out - último a entrar, primeiro a sair)