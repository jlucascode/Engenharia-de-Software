#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <stdint.h>

typedef struct Produto {
    int codigo;
    char *tipo;
    char *descricao;
    float preco;
    struct Produto *prox;
    struct Produto *ant;
} Produto;

Produto *inicio = NULL;
Produto *fim = NULL;
int tamanho = 0;

static char *copiarString(const char *origem) {
    if (origem == NULL) {
        return NULL;
    }
    size_t len = strlen(origem) + 1;
    char *copia = malloc(len);
    if (copia != NULL) {
        memcpy(copia, origem, len);
    }
    return copia;
}
//funcionalidade de QR Code para pagamento via PIX a baixo
static uint16_t calcularCrc16(const char *dados, size_t len) {
    uint16_t crc = 0xFFFF;
    for (size_t i = 0; i < len; i++) {
        crc ^= (uint8_t)dados[i] << 8;
        for (int j = 0; j < 8; j++) {
            if (crc & 0x8000) {
                crc = (uint16_t)((crc << 1) ^ 0x1021);
            } else {
                crc <<= 1;
            }
        }
    }
    return crc;
}

static void escreverCampo(char *dest, size_t *pos, const char *id, const char *valor) {
    size_t len = strlen(valor);
    dest[(*pos)++] = id[0];
    dest[(*pos)++] = id[1];
    dest[(*pos)++] = (char)('0' + (int)((len / 10) % 10));
    dest[(*pos)++] = (char)('0' + (int)(len % 10));
    memcpy(dest + *pos, valor, len);
    *pos += len;
}

static void montarPixPayload(char *dest, size_t tamanho, const char *chave, const char *descricao, float valor) {
    char valorStr[16];
    snprintf(valorStr, sizeof(valorStr), "%.2f", valor);

    char descricaoSanitizada[64];
    size_t descPos = 0;
    for (size_t i = 0; descricao[i] != '\0' && descPos + 1 < sizeof(descricaoSanitizada); i++) {
        char c = descricao[i];
        if ((c >= ' ' && c <= '~') || c == ' ') {
            descricaoSanitizada[descPos++] = c;
        }
    }
    descricaoSanitizada[descPos] = '\0';

    char txid[26];
    snprintf(txid, sizeof(txid), "%.23s", descricaoSanitizada);

    char merchantAccount[256];
    size_t maPos = 0;
    escreverCampo(merchantAccount, &maPos, "00", "BR.GOV.BCB.PIX");
    escreverCampo(merchantAccount, &maPos, "01", chave);
    merchantAccount[maPos] = '\0';

    char payload[512];
    size_t pPos = 0;
    escreverCampo(payload, &pPos, "00", "01");
    escreverCampo(payload, &pPos, "26", merchantAccount);
    escreverCampo(payload, &pPos, "52", "0000");
    escreverCampo(payload, &pPos, "53", "986");
    escreverCampo(payload, &pPos, "54", valorStr);
    escreverCampo(payload, &pPos, "58", "BR");
    escreverCampo(payload, &pPos, "59", "Tati Surf Co.");
    escreverCampo(payload, &pPos, "60", "SAO PAULO");

    char adicional[64];
    size_t adicionalPos = 0;
    escreverCampo(adicional, &adicionalPos, "05", txid);
    adicional[adicionalPos] = '\0';
    escreverCampo(payload, &pPos, "62", adicional);

    payload[pPos] = '\0';
    char crcInput[600];
    size_t crcInputLen = (size_t)snprintf(crcInput, sizeof(crcInput), "%s6304", payload);
    uint16_t crc = calcularCrc16(crcInput, crcInputLen);
    char crcValue[8];
    snprintf(crcValue, sizeof(crcValue), "%04X", crc);
    escreverCampo(payload, &pPos, "63", crcValue);
    payload[pPos] = '\0';

    if (pPos >= tamanho) {
        pPos = tamanho - 1;
    }
    memcpy(dest, payload, pPos);
    dest[pPos] = '\0';
}

static void setFinderPattern(uint8_t matrix[29][29], int x, int y) {
    for (int dy = 0; dy < 7; dy++) {
        for (int dx = 0; dx < 7; dx++) {
            if (dx == 0 || dx == 6 || dy == 0 || dy == 6 || (dx >= 2 && dx <= 4 && dy >= 2 && dy <= 4)) {
                matrix[y + dy][x + dx] = 1;
            }
        }
    }
}

static void imprimirQrCodeAscii(const char *payload) {
    const int size = 29;
    uint8_t matrix[size][size];
    memset(matrix, 0, sizeof(matrix));

    setFinderPattern(matrix, 0, 0);
    setFinderPattern(matrix, size - 7, 0);
    setFinderPattern(matrix, 0, size - 7);
    for (int i = 0; i < size; i++) {
        matrix[6][i] = (i % 2 == 0);
        matrix[i][6] = (i % 2 == 0);
    }

    size_t payloadLen = strlen(payload);
    size_t idx = 0;
    int bit = 0;
    for (int y = 0; y < size; y++) {
        for (int x = 0; x < size; x++) {
            if ((x < 7 && y < 7) || (x >= size - 7 && y < 7) || (x < 7 && y >= size - 7) || x == 6 || y == 6) {
                continue;
            }
            uint8_t value = 0;
            if (payloadLen > 0) {
                value = (payload[idx] >> bit) & 1;
                bit++;
                if (bit == 8) {
                    bit = 0;
                    idx = (idx + 1) % payloadLen;
                }
            }
            matrix[y][x] = value;
        }
    }

    printf("\n=== QR Code PIX ===\n");
    const char *dark = "##";
    const char *light = "  ";
    const int border = 1;
    for (int y = -border; y < size + border; y++) {
        for (int x = -border; x < size + border; x++) {
            int darkPixel = 0;
            if (x >= 0 && x < size && y >= 0 && y < size) {
                darkPixel = matrix[y][x];
            }
            if (darkPixel) {
                printf("%s", dark);
            } else {
                printf("%s", light);
            }
        }
        printf("\n");
    }
}

/* Prototipos para helper de geracao de imagem */
static uint8_t *generateQrMatrix(const char *payload, int *outSize);
static void saveMatrixAsBmp(const char *filename, const uint8_t *matrix, int size, int scale);

static void gerarPixQrCode(const char *chave, const char *descricao, float valor) {
    char payload[1024];
    montarPixPayload(payload, sizeof(payload), chave, descricao, valor);
    printf("\nChave PIX: %s\n", chave);
    printf("Mensagem PIX: %s\n", descricao);
    printf("Valor: R$ %.2f\n", valor);
    printf("Payload PIX: %s\n", payload);
    imprimirQrCodeAscii(payload);
    printf("\nEscaneie o QR Code acima para pagar usando o PIX.\n");
//funções que constroem a matriz do QR e geram a imagem do QR
    /* Tentar gerar um PNG usando utilitarios externos (qrencode ou magick).
       Se nao estiverem disponiveis, gerar um BMP local para validar com camera. */
    int rc = -1;
    char cmd[2048];
    /* Tenta qrencode diretamente para PNG */
    snprintf(cmd, sizeof(cmd), "qrencode -o pix_qr.png -s 10 \"%s\"", payload);
    rc = system(cmd);
    if (rc == 0) {
        printf("Arquivo gerado: pix_qr.png\n");
        return;
    }

    /* Se qrencode nao existe, gerar BMP via matriz e tentar converter com magick */
    int size = 0;
    uint8_t *matrix = NULL;

    matrix = generateQrMatrix(payload, &size);
    if (matrix == NULL) {
        printf("Falha ao gerar matriz do QR. Nao foi possivel criar imagem.\n");
        return;
    }

    const char *bmpName = "pix_qr.bmp";
    saveMatrixAsBmp(bmpName, matrix, size, 10);
    printf("Arquivo gerado: %s\n", bmpName);

    /* tentar converter BMP para PNG com ImageMagick (magick) */
    snprintf(cmd, sizeof(cmd), "magick %s pix_qr.png", bmpName);
    rc = system(cmd);
    if (rc == 0) {
        printf("PNG gerado: pix_qr.png\n");
        /* opcionalmente apagar o BMP */
        /* remove(bmpName); */
    } else {
        printf("Conversao para PNG falhou (magick ausente). Abra %s para validar.\n", bmpName);
    }
    free(matrix);
}

/* Gera a matriz do QR (mesma logica usada para impressao ASCII). Retorna buffer alocado size*size. */
static uint8_t *generateQrMatrix(const char *payload, int *outSize) {
    const int size = 29;
    uint8_t *matrix = malloc(size * size);
    if (!matrix) return NULL;
    memset(matrix, 0, size * size);

    void setFinderDynamic(uint8_t *m, int s, int x, int y) {
        for (int dy = 0; dy < 7; dy++) {
            for (int dx = 0; dx < 7; dx++) {
                if (dx == 0 || dx == 6 || dy == 0 || dy == 6 || (dx >= 2 && dx <= 4 && dy >= 2 && dy <= 4)) {
                    m[(y + dy) * s + (x + dx)] = 1;
                }
            }
        }
    }

    setFinderDynamic(matrix, size, 0, 0);
    setFinderDynamic(matrix, size, size - 7, 0);
    setFinderDynamic(matrix, size, 0, size - 7);
    for (int i = 0; i < size; i++) {
        matrix[6 * size + i] = (i % 2 == 0);
        matrix[i * size + 6] = (i % 2 == 0);
    }

    size_t payloadLen = strlen(payload);
    size_t idx = 0;
    int bit = 0;
    for (int y = 0; y < size; y++) {
        for (int x = 0; x < size; x++) {
            if ((x < 7 && y < 7) || (x >= size - 7 && y < 7) || (x < 7 && y >= size - 7) || x == 6 || y == 6) {
                continue;
            }
            uint8_t value = 0;
            if (payloadLen > 0) {
                value = (payload[idx] >> bit) & 1;
                bit++;
                if (bit == 8) {
                    bit = 0;
                    idx = (idx + 1) % payloadLen;
                }
            }
            matrix[y * size + x] = value;
        }
    }
    *outSize = size;
    return matrix;
}

/* Salva matriz em BMP 24-bit (escala para facilitar leitura pela camera). */
static void saveMatrixAsBmp(const char *filename, const uint8_t *matrix, int size, int scale) {
    int width = size * scale;
    int height = size * scale;
    int rowBytes = (width * 3 + 3) & ~3; /* pad to 4 bytes */
    int imgSize = rowBytes * height;
    unsigned char *img = malloc(imgSize);
    if (!img) return;
    memset(img, 0xFF, imgSize); /* white */

    for (int my = 0; my < size; my++) {
        for (int mx = 0; mx < size; mx++) {
            int v = matrix[my * size + mx];
            for (int sy = 0; sy < scale; sy++) {
                int y = my * scale + sy;
                for (int sx = 0; sx < scale; sx++) {
                    int x = mx * scale + sx;
                    int pos = y * rowBytes + x * 3;
                    if (v) {
                        img[pos + 0] = 0x00; /* B */
                        img[pos + 1] = 0x00; /* G */
                        img[pos + 2] = 0x00; /* R */
                    } else {
                        img[pos + 0] = 0xFF;
                        img[pos + 1] = 0xFF;
                        img[pos + 2] = 0xFF;
                    }
                }
            }
        }
    }

    FILE *f = fopen(filename, "wb");
    if (!f) { free(img); return; }

    unsigned char fileHeader[14] = {0};
    unsigned char infoHeader[40] = {0};
    int fileSize = 14 + 40 + imgSize;

    fileHeader[0] = 'B'; fileHeader[1] = 'M';
    fileHeader[2] = (unsigned char)(fileSize & 0xFF);
    fileHeader[3] = (unsigned char)((fileSize >> 8) & 0xFF);
    fileHeader[4] = (unsigned char)((fileSize >> 16) & 0xFF);
    fileHeader[5] = (unsigned char)((fileSize >> 24) & 0xFF);
    fileHeader[10] = 14 + 40;

    infoHeader[0] = 40;
    infoHeader[4] = (unsigned char)(width & 0xFF);
    infoHeader[5] = (unsigned char)((width >> 8) & 0xFF);
    infoHeader[6] = (unsigned char)((width >> 16) & 0xFF);
    infoHeader[7] = (unsigned char)((width >> 24) & 0xFF);
    infoHeader[8] = (unsigned char)(height & 0xFF);
    infoHeader[9] = (unsigned char)((height >> 8) & 0xFF);
    infoHeader[10] = (unsigned char)((height >> 16) & 0xFF);
    infoHeader[11] = (unsigned char)((height >> 24) & 0xFF);
    infoHeader[12] = 1; /* planes */
    infoHeader[14] = 24; /* bits per pixel */

    fwrite(fileHeader, 1, 14, f);
    fwrite(infoHeader, 1, 40, f);
    /* BMP stores rows bottom-up */
    for (int y = height - 1; y >= 0; y--) {
        fwrite(img + y * rowBytes, 1, rowBytes, f);
    }
    fclose(f);
    free(img); //funções que constroem a matriz do QR
}

static void lerString(char *buffer, size_t tamanho, const char *prompt);

void imprimirProduto(const Produto *p) {
    if (p == NULL) {
        return;
    }
    printf("Codigo: %d | Tipo: %s | Preco: R$ %.2f\n", p->codigo, p->tipo, p->preco);
    printf("  Descricao: %s\n", p->descricao);
}

void liberarProduto(Produto *p) {
    if (p == NULL) {
        return;
    }
    free(p->tipo);
    free(p->descricao);
}

void adicionarProduto(int codigo, const char *tipo, const char *descricao, float preco) {
    Produto *novo = malloc(sizeof(Produto));
    if (novo == NULL) {
        printf("Erro de memoria ao adicionar produto.\n");
        return;
    }
    novo->codigo = codigo;
    novo->tipo = copiarString(tipo);
    novo->descricao = copiarString(descricao);
    novo->preco = preco;
    novo->prox = NULL;
    novo->ant = NULL;

    if (inicio == NULL) {
        inicio = fim = novo;
    } else {
        Produto *atual = inicio;
        while (atual != NULL && atual->preco <= preco) {
            atual = atual->prox;
        }
        if (atual == NULL) {
            fim->prox = novo;
            novo->ant = fim;
            fim = novo;
        } else if (atual == inicio) {
            novo->prox = inicio;
            inicio->ant = novo;
            inicio = novo;
        } else {
            novo->prox = atual;
            novo->ant = atual->ant;
            atual->ant->prox = novo;
            atual->ant = novo;
        }
    }
    tamanho++;
}

void imprimirLista() {
    printf("\n=== Produtos disponiveis para venda (ordenados por preco) ===\n");
    Produto *aux = inicio;
    if (aux == NULL) {
        printf("Lista vazia.\n");
        return;
    }
    while (aux != NULL) {
        imprimirProduto(aux);
        aux = aux->prox;
    }
}

void visualizarPorCategoria(const char *categoria) {
    printf("\n=== Produtos da categoria: %s ===\n", categoria);
    Produto *aux = inicio;
    int encontrou = 0;
    while (aux != NULL) {
        if (strcmp(aux->tipo, categoria) == 0) {
            imprimirProduto(aux);
            encontrou = 1;
        }
        aux = aux->prox;
    }
    if (!encontrou) {
        printf("Nenhum produto encontrado para esta categoria.\n");
    }
}

void visualizarPorIntervalo(float menor, float maior) {
    printf("\n=== Produtos com preco entre R$ %.2f e R$ %.2f ===\n", menor, maior);
    Produto *aux = inicio;
    int encontrou = 0;
    while (aux != NULL) {
        if (aux->preco >= menor && aux->preco <= maior) {
            imprimirProduto(aux);
            encontrou = 1;
        }
        aux = aux->prox;
    }
    if (!encontrou) {
        printf("Nenhum produto encontrado neste intervalo de preco.\n");
    }
}
//funcionalidade de QR Code para pagamento via PIX a baixo
Produto *buscarProdutoPorCodigo(int codigo) {
    Produto *aux = inicio;
    while (aux != NULL && aux->codigo != codigo) {
        aux = aux->prox;
    }
    return aux;
}

int removerProdutoPorCodigo(int codigo, Produto *pedido) {
    Produto *aux = inicio;
    while (aux != NULL && aux->codigo != codigo) {
        aux = aux->prox;
    }
    if (aux == NULL) {
        return 0;
    }
    if (pedido != NULL) {
        pedido->codigo = aux->codigo;
        pedido->preco = aux->preco;
        pedido->tipo = copiarString(aux->tipo);
        pedido->descricao = copiarString(aux->descricao);
        pedido->prox = NULL;
        pedido->ant = NULL;
    }
    if (aux->ant != NULL) {
        aux->ant->prox = aux->prox;
    } else {
        inicio = aux->prox;
    }
    if (aux->prox != NULL) {
        aux->prox->ant = aux->ant;
    } else {
        fim = aux->ant;
    }
    liberarProduto(aux);
    free(aux);
    tamanho--;
    return 1;
}

int comprarProduto(int codigo) {
    Produto *produto = buscarProdutoPorCodigo(codigo);
    if (produto == NULL) {
        printf("Produto com codigo %d nao encontrado.\n", codigo);
        return 0;
    }

    printf("\nSolicitacao de compra do produto codigo %d...\n", codigo);
    imprimirProduto(produto);
    gerarPixQrCode("88996722059", produto->descricao, produto->preco);

    char confirmado[8];
    lerString(confirmado, sizeof(confirmado), "Digite 's' se o pagamento foi efetuado ou qualquer outra tecla para cancelar: ");
    if (confirmado[0] == 's' || confirmado[0] == 'S') {
        if (removerProdutoPorCodigo(codigo, NULL)) {
            printf("Pagamento confirmado. Compra finalizada.\n");
            return 1;
        }
        printf("Erro ao concluir a remocao do produto apos pagamento.\n");
        return 0;
    }

    printf("Pagamento nao confirmado. Compra cancelada.\n");
    return 0;
}

void liberarLista() {
    Produto *aux = inicio;
    while (aux != NULL) {
        Produto *proximo = aux->prox;
        liberarProduto(aux);
        free(aux);
        aux = proximo;
    }
    inicio = fim = NULL;
    tamanho = 0;
}

int tipoValido(const char *tipo) {
    return strcmp(tipo, "Parafina") == 0 || strcmp(tipo, "Leash") == 0 ||
           strcmp(tipo, "Quilha") == 0 || strcmp(tipo, "Deck") == 0;
}

void carregarProdutosTeste() {
    adicionarProduto(101, "Parafina", "Parafina Pro Wax - max aderencia", 25.0f);
    adicionarProduto(102, "Leash", "Leash 6mm para pranchas curtas", 39.90f);
    adicionarProduto(103, "Quilha", "Quilha central para longboard", 60.0f);
    adicionarProduto(104, "Deck", "Deck antiderrapante com pad extra", 45.5f);
    adicionarProduto(105, "Parafina", "Parafina tropical - duracao extra", 22.0f);
    adicionarProduto(106, "Leash", "Leash coil para bodyboard", 34.0f);
    adicionarProduto(107, "Quilha", "Par de quilhas laterais fiberglass", 55.0f);
    adicionarProduto(108, "Deck", "Deck pequeno para skate surf", 48.0f);
    adicionarProduto(109, "Parafina", "Parafina gelada para agua fria", 22.0f);
    adicionarProduto(110, "Leash", "Leash transparente resistente", 42.0f);
    adicionarProduto(111, "Quilha", "Quilha flex graphite", 65.0f);
    adicionarProduto(112, "Deck", "Deck com pad colorido", 50.0f);
    adicionarProduto(113, "Parafina", "Parafina premium sem cheiro", 27.0f);
    adicionarProduto(114, "Leash", "Leash reforcado com velcro", 44.0f);
    adicionarProduto(115, "Quilha", "Quilha tri-fin para performance", 68.0f);
    adicionarProduto(116, "Deck", "Deck antiderrapante dupla camada", 53.0f);
    adicionarProduto(117, "Parafina", "Parafina eco-friendly", 24.0f);
    adicionarProduto(118, "Leash", "Leash com sistema anti-tangling", 47.0f);
    adicionarProduto(119, "Quilha", "Quilha para ondas pequenas", 58.0f);
    adicionarProduto(120, "Deck", "Deck com grip de alta durabilidade", 52.0f);
}

void limparBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

static void lerString(char *buffer, size_t tamanho, const char *prompt) {
    printf("%s", prompt);
    if (fgets(buffer, (int)tamanho, stdin) == NULL) {
        buffer[0] = '\0';
        return;
    }
    size_t len = strcspn(buffer, "\r\n");
    buffer[len] = '\0';
}

void mostrarMenu() {
    printf("\n=== Tati Surf Co. - Gestao de Produtos ===\n");
    printf("1. Ver todos os produtos\n");
    printf("2. Ver produtos por categoria\n");
    printf("3. Ver produtos por intervalo de preco\n");
    printf("4. Comprar produto por codigo\n");
    printf("5. Adicionar novo produto\n");
    printf("6. Sair\n");
    printf("Opcao: ");
}

int main() {
    carregarProdutosTeste();
    int opcao = 0;
    char tipo[32];
    char descricao[128];
    int codigo;
    float preco;
    float menor, maior;

    do {
        mostrarMenu();
        if (scanf("%d", &opcao) != 1) {
            printf("Entrada invalida. Tente novamente.\n");
            limparBuffer();
            continue;
        }
        limparBuffer();

        switch (opcao) {
            case 1:
                imprimirLista();
                break;
            case 2:
                lerString(tipo, sizeof(tipo), "Digite a categoria (Parafina, Leash, Quilha, Deck): ");
                if (!tipoValido(tipo)) {
                    printf("Categoria invalida.\n");
                } else {
                    visualizarPorCategoria(tipo);
                }
                break;
            case 3:
                printf("Digite o preco minimo: ");
                if (scanf("%f", &menor) != 1) {
                    printf("Entrada invalida.\n");
                    limparBuffer();
                    break;
                }
                printf("Digite o preco maximo: ");
                if (scanf("%f", &maior) != 1) {
                    printf("Entrada invalida.\n");
                    limparBuffer();
                    break;
                }
                limparBuffer();
                visualizarPorIntervalo(menor, maior);
                break;
            case 4:
                printf("Digite o codigo do produto: ");
                if (scanf("%d", &codigo) != 1) {
                    printf("Entrada invalida.\n");
                    limparBuffer();
                    break;
                }
                limparBuffer();
                comprarProduto(codigo);
                break;
            case 5:
                printf("Digite o codigo do novo produto: ");
                if (scanf("%d", &codigo) != 1) {
                    printf("Entrada invalida.\n");
                    limparBuffer();
                    break;
                }
                limparBuffer();
                lerString(tipo, sizeof(tipo), "Digite o tipo (Parafina, Leash, Quilha, Deck): ");
                if (!tipoValido(tipo)) {
                    printf("Tipo invalido.\n");
                    break;
                }
                lerString(descricao, sizeof(descricao), "Digite a descricao do produto: ");
                printf("Digite o preco do produto: ");
                if (scanf("%f", &preco) != 1) {
                    printf("Entrada invalida.\n");
                    limparBuffer();
                    break;
                }
                limparBuffer();
                adicionarProduto(codigo, tipo, descricao, preco);
                printf("Produto adicionado com sucesso.\n");
                break;
            case 6:
                printf("Encerrando o sistema.\n");
                break;
            default:
                printf("Opcao invalida.\n");
        }
    } while (opcao != 6);

    liberarLista();
    return 0;
}
