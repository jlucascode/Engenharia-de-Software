#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main() {
    int a, b;
    printf("Enter two integers: ");
    scanf("%d %d", &a, &b);
    
    int sum = a + b;
    printf("The sum of %d and %d is %d\n", a, b, sum);
    
    return 0;
}
 