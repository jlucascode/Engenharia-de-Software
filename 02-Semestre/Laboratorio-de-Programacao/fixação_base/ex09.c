/*#include <stdio.h>
int main() {
    float m;
    printf("Metros: ");
    scanf("%f", &m);
    printf("%.1f dm | %.1f cm | %.1f mm", m*10, m*100, m*1000);
    return 0;
}*/
#include <stdio.h>
int main() {
    float km;
    printf("Kilometros: ");
    scanf("%f", &km);
    printf("%.1f m | %.1f dm | %.1f cm | %.1f mm", km*1000, km*10000, km*100000, km*1000000);
    return 0;
}
