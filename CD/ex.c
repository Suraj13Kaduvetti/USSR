#include <stdio.h>

void switch_case_example(int value) {
    switch (value) {
        case 1:
            printf("Case 1\n");
            break;
        case 2:
            printf("Case 2\n");
            break;
        case 3:
            printf("Case 3\n");
            break;
        default:
            printf("Default case\n");
    }
}

int main() {
    int value = 2;
    switch_case_example(value);
    return 0;
}
