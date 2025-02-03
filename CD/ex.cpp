#include <iostream>

void switch_case_example(int value) {
    switch (value) {
        case 1:
            std::cout << "Case 1" << std::endl;
            break;
        case 2:
            std::cout << "Case 2" << std::endl;
            break;
        case 3:
            std::cout << "Case 3" << std::endl;
            break;
        default:
            std::cout << "Default case" << std::endl;
    }
}

int main() {
    int value = 3;
    switch_case_example(value);
    return 0;
}
