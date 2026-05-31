#include <stdio.h>
int main() {
    float m;
    printf("Metros: ");
    scanf("%f", &m);
    printf("%.1f dm | %.1f cm | %.1f mm", m*10, m*100, m*1000);
    return 0;
}
