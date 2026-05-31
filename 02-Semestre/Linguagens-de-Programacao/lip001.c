#include <stdio.h>

int main(void) {
    int a = 2;
    int b = 3;
    int *p;
    int x;
    p = &b;
    x = a + b;
    printf("Value: %p\n", (void *)&p);
    printf("Value: %p\n", (void *)p);
    printf("Value: %d\n", *p);
    printf("Value: %d\n", x);
    return 0;
}