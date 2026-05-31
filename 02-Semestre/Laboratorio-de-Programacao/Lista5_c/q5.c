#include <stdio.h>

int main() {
    int i = 3, j = 5;
    int *p, *q;
    p = &i;
    q = &j;

    // Expressao: *p - *q
    // *p = valor apontado por p = i = 3
    // *q = valor apontado por q = j = 5
    // *p - *q = 3 - 5 = -2

    printf("*p - *q = %d\n", *p - *q); // -2

    return 0;
}
