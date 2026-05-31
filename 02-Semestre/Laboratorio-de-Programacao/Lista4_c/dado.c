#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int Dado() {
    return (rand() % 6) + 1;
}

int main() {
    srand(time(NULL));
    printf("Resultado do dado: %d\n", Dado());
    return 0;
}
