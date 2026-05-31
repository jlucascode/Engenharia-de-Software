#include <stdio.h>
#include <stdlib.h>

int main() {
    int month, year;

    printf("Enter month (1-12): ");
    scanf("%d", &month);

    printf("Enter year: ");
    scanf("%d", &year);

    if (month < 1 || month > 12) {
        printf("Invalid month. Please enter a value between 1 and 12.\n");
        return 1;
    }

    int daysInMonth;

    switch (month) {
        case 1: case 3: case 5: case 7: case 8: case 10: case 12:
            daysInMonth = 31;
            break;
        case 4: case 6: case 9: case 11:
            daysInMonth = 30;
            break;
        case 2:
            if ((year % 4 == 0 && year % 100 != 0) || (year % 400 == 0)) {
                daysInMonth = 29; // Leap year
            } else {
                daysInMonth = 28; // Non-leap year
            }
            break;
        default: 
            printf("Invalid month.\n");
            return 1;
    }

    printf("Number of days in month %d of year %d is: %d\n", month, year, daysInMonth);
    return 0;
}