#include <stdlib.h>
#include <stdio.h>

typedef struct NO{

    //dados da aplicacao
    int operando;

    //mecanismo de uniao de nos
    struct NO * prox;

}NO;

NO *topo = NULL;
int tam = 0;

void add(int operando){

        NO * novo = malloc(sizeof(NO));
        novo->operando = operando;
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
        printf("Operando: %d \n", aux->operando);
        //... fazer os demais dados
        aux = aux->prox;
    }
}

int remover(){

        if(tam > 0){ //piha tem elementos
            NO *lixo = topo;
            int operando = lixo->operando;
            topo = topo->prox;
            free(lixo);
            tam--;
            return operando;
        }else{
            printf("Pilha esta sem elementos para remocao! :)");
            return 0;
        }

}

int avaliar_pos_fixa(const char *expressao_mat){
    const char *p = expressao_mat;
    while (*p != '\0') {
        while (*p == ' ' || *p == '\t' || *p == '\n') {
            p++;
        }
        if (*p == '\0') {
            break;
        }

        if ((*p >= '0' && *p <= '9') || ((*p == '+' || *p == '-') && (p[1] >= '0' && p[1] <= '9'))) {
            char *endptr;
            long valor = strtol(p, &endptr, 10);
            add((int)valor);
            p = endptr;
        } else {
            int b = remover();
            int a = remover();
            int resultado = 0;

            switch (*p) {
                case '+': resultado = a + b; break;
                case '-': resultado = a - b; break;
                case '*': resultado = a * b; break;
                case '/':
                    if (b == 0) {
                        printf("Erro: divisao por zero.\n");
                        return 0;
                    }
                    resultado = a / b;
                    break;
                default:
                    printf("Erro: operador invalido '%c'.\n", *p);
                    return 0;
            }
            add(resultado);
            p++;
        }
    }

    if (tam != 1) {
        printf("Erro: expressao invalida.\n");
        return 0;
    }
    return remover();
}

int main(){
    char expressao[256];
    printf("Digite a expressao pos-fixa (ex: 1 2 - 4 5 + *): \n");
    if (fgets(expressao, sizeof(expressao), stdin) == NULL) {
        return 1;
    }

    int resultado = avaliar_pos_fixa(expressao);
    printf("Resultado: %d\n", resultado);
    return 0;
}