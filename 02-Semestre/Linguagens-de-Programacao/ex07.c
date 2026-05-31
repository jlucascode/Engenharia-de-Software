#include <stdio.h>
int main() {
    int total_seg, h, m, s;
    printf("Total de segundos: ");
    scanf("%d", &total_seg);
    h = total_seg / 3600;       
    m = (total_seg % 3600) / 60; 
    s = total_seg % 60;          
    printf("%02d:%02d:%02d", h, m, s); // O %02d faz aparecer 01:05 em vez de 1:5
    return 0;
}