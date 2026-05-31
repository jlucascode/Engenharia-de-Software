#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct NO{
    int code_product;
    char tipo_produto[20];
    char descricao_produto[100];
    float preco;
    struct NO *prox;
    struct NO *ant;
} NO;

NO *inicio = NULL;
NO *fim = NULL;
int tam = 0;

void add(int code_product, const char *tipo_produto, const char *descricao_produto, float preco){
    NO *novo = malloc(sizeof(NO));
    if(novo == NULL){
        printf("Erro de alocacao de memoria.\n");
        return;
    }

    novo->code_product = code_product;
    strncpy(novo->tipo_produto, tipo_produto, sizeof(novo->tipo_produto) - 1);
    novo->tipo_produto[sizeof(novo->tipo_produto) - 1] = '\0';
    strncpy(novo->descricao_produto, descricao_produto, sizeof(novo->descricao_produto) - 1);
    novo->descricao_produto[sizeof(novo->descricao_produto) - 1] = '\0';
    novo->preco = preco;
    novo->prox = NULL;
    novo->ant = NULL;

    if(inicio == NULL){
        inicio = novo;
        fim = novo;
    } else if(preco < inicio->preco){
        novo->prox = inicio;
        inicio->ant = novo;
        inicio = novo;
    } else {
        NO *aux = inicio;
        while(aux->prox != NULL && aux->prox->preco <= preco){
            aux = aux->prox;
        }

        if(aux->prox == NULL){
            aux->prox = novo;
            novo->ant = aux;
            fim = novo;
        } else {
            novo->prox = aux->prox;
            novo->ant = aux;
            aux->prox->ant = novo;
            aux->prox = novo;
        }
    }

    tam++;
}

void imprimir(){
    NO *aux = inicio;
    if(aux == NULL){
        printf("Lista vazia.\n\n");
        return;
    }

    printf("Produtos disponiveis para venda:\n");
    while(aux != NULL){
        printf("Codigo: %d | Tipo: %s | Descricao: %s | Preco: %.2f\n",
               aux->code_product, aux->tipo_produto, aux->descricao_produto, aux->preco);
        aux = aux->prox;
    }
    printf("\n");
}

void listarPorCategoria(const char *tipo){
    NO *aux = inicio;
    printf("Produtos da categoria '%s':\n", tipo);
    while(aux != NULL){
        if(strcmp(aux->tipo_produto, tipo) == 0){
            printf("Codigo: %d | Tipo: %s | Descricao: %s | Preco: %.2f\n",
                   aux->code_product, aux->tipo_produto, aux->descricao_produto, aux->preco);
        }
        aux = aux->prox;
    }
    printf("\n");
}

void listarPorIntervalo(float min, float max){
    NO *aux = inicio;
    printf("Produtos com preco entre %.2f e %.2f:\n", min, max);
    while(aux != NULL){
        if(aux->preco >= min && aux->preco <= max){
            printf("Codigo: %d | Tipo: %s | Descricao: %s | Preco: %.2f\n",
                   aux->code_product, aux->tipo_produto, aux->descricao_produto, aux->preco);
        }
        aux = aux->prox;
    }
    printf("\n");
}

NO *remover(int code_product){
    NO *aux = inicio;
    while(aux != NULL && aux->code_product != code_product){
        aux = aux->prox;
    }

    if(aux == NULL){
        return NULL;
    }

    if(aux->ant != NULL){
        aux->ant->prox = aux->prox;
    } else {
        inicio = aux->prox;
    }

    if(aux->prox != NULL){
        aux->prox->ant = aux->ant;
    } else {
        fim = aux->ant;
    }

    aux->prox = NULL;
    aux->ant = NULL;
    tam--;
    return aux;
}

void liberarLista(){
    NO *aux = inicio;
    while(aux != NULL){
        NO *prox = aux->prox;
        free(aux);
        aux = prox;
    }
    inicio = NULL;
    fim = NULL;
    tam = 0;
}

int main() {
  
    add(101, "Parafina", "Parafina para surf - marca A", 45.50);
    add(102, "Leash", "Leash de seguranca 6 ft", 35.00);
    add(103, "Quilha", "Quilha central em fibra de vidro", 55.00);
    add(104, "Deck", "Deck antiderrapante tamanho medio", 72.90);
    add(105, "Parafina", "Parafina tropical", 28.00);
    add(106, "Leash", "Leash comfort com rotacao", 42.00);
    add(107, "Quilha", "Kit de 3 quilhas pequenas", 66.50);
    add(108, "Deck", "Deck antiderrapante colorido", 59.90);
    add(109, "Parafina", "Parafina action", 32.00);
    add(110, "Leash", "Leash para prancha funboard", 38.75);
    add(111, "Quilha", "Quilha grande para performance", 82.00);
    add(112, "Deck", "Deck premium pro", 92.40);
    add(113, "Parafina", "Parafina anti-derrapante", 25.00);
    add(114, "Leash", "Leash para longboard", 49.90);
    add(115, "Quilha", "Quilha central para surf rapido", 58.00);
    add(116, "Deck", "Deck antiderrapante para iniciantes", 68.50);
    add(117, "Parafina", "Parafina refrescante", 30.00);
    add(118, "Leash", "Leash gel", 33.00);
    add(119, "Quilha", "Quilha versatil em nylon", 61.20);
    add(120, "Deck", "Deck antiderrapante pequeno", 47.80);

    imprimir();

    listarPorCategoria("Parafina");
    listarPorIntervalo(30.00f, 60.00f);

    NO *produtoRemovido;

    produtoRemovido = remover(103);
    if(produtoRemovido != NULL){
        printf("Produto comprado: %d | %s | %s | %.2f\n\n",
               produtoRemovido->code_product,
               produtoRemovido->tipo_produto,
               produtoRemovido->descricao_produto,
               produtoRemovido->preco);
        free(produtoRemovido);
    }

    produtoRemovido = remover(110);
    if(produtoRemovido != NULL){
        printf("Produto comprado: %d | %s | %s | %.2f\n\n",
               produtoRemovido->code_product,
               produtoRemovido->tipo_produto,
               produtoRemovido->descricao_produto,
               produtoRemovido->preco);
        free(produtoRemovido);
    }

    produtoRemovido = remover(115);
    if(produtoRemovido != NULL){
        printf("Produto comprado: %d | %s | %s | %.2f\n\n",
               produtoRemovido->code_product,
               produtoRemovido->tipo_produto,
               produtoRemovido->descricao_produto,
               produtoRemovido->preco);
        free(produtoRemovido);
    }

    produtoRemovido = remover(118);
    if(produtoRemovido != NULL){
        printf("Produto comprado: %d | %s | %s | %.2f\n\n",
               produtoRemovido->code_product,
               produtoRemovido->tipo_produto,
               produtoRemovido->descricao_produto,
               produtoRemovido->preco);
        free(produtoRemovido);
    }

    produtoRemovido = remover(120);
    if(produtoRemovido != NULL){
        printf("Produto comprado: %d | %s | %s | %.2f\n\n",
               produtoRemovido->code_product,
               produtoRemovido->tipo_produto,
               produtoRemovido->descricao_produto,
               produtoRemovido->preco);
        free(produtoRemovido);
    }

    printf("Lista apos compras:\n");
    imprimir();

    liberarLista();
    return 0;
}