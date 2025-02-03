#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

#define MAX_EXPR_LENGTH 100

// Structure to represent a variable or constant
typedef struct {
    char name[MAX_EXPR_LENGTH]; // Variable name (empty if it's a number)
    int value;                  // The value for constants (0 for variables)
    int is_variable;            // 1 if it's a variable, 0 if it's a constant
} Operand;

// Structure to represent a quadruple (operator, operand1, operand2, result)
typedef struct {
    char operator;
    char operand1[MAX_EXPR_LENGTH];
    char operand2[MAX_EXPR_LENGTH];
    char result[MAX_EXPR_LENGTH];
} Quadruple;

// Function to print the 3-address code for the operation
void generate_TAC(char operator, Operand op1, Operand op2, int t3) {
    if (op1.is_variable) {
        printf("%s", op1.name); // Variable name on the left side
    } else {
        printf("%d", op1.value); // Constant value on the left side
    }

    if (op2.is_variable) {
        printf(" %c %s", operator, op2.name); // Variable name on the right side
    } else {
        printf(" %c %d", operator, op2.value); // Constant value on the right side
    }

    printf(" => t%d\n", t3); // Store the result in a temporary variable
}

// Function to handle the assignment
void generate_assignment_TAC(const char* var, int t3) {
    printf("%s = t%d\n", var, t3); // Generate the assignment statement
}

// Function to evaluate precedence of operators
int precedence(char operator) {
    if (operator == '+' || operator == '-') {
        return 1;
    }
    if (operator == '*' || operator == '/') {
        return 2;
    }
    return 0;
}

// Function to perform the arithmetic operation
int perform_operation(int t1, int t2, char operator) {
    switch (operator) {
        case '+': return t1 + t2;
        case '-': return t1 - t2;
        case '*': return t1 * t2;
        case '/': return t1 / t2;
        default: return 0;
    }
}

// Function to generate a quadruple
void generate_quadruple(char operator, Operand op1, Operand op2, int t3, Quadruple *quadruples, int *quadruple_count) {
    Quadruple quad;
    quad.operator = operator;
    if (op1.is_variable) {
        strcpy(quad.operand1, op1.name);
    } else {
        sprintf(quad.operand1, "%d", op1.value);
    }
    if (op2.is_variable) {
        strcpy(quad.operand2, op2.name);
    } else {
        sprintf(quad.operand2, "%d", op2.value);
    }
    sprintf(quad.result, "t%d", t3);

    // Add the quadruple to the list
    quadruples[*quadruple_count] = quad;
    (*quadruple_count)++;
}

// Function to print all quadruples
void print_quadruples(Quadruple *quadruples, int quadruple_count) {
    printf("\nQuadruples:\n");
    printf("Op\tOperand1\tOperand2\tResult\n");
    for (int i = 0; i < quadruple_count; i++) {
        printf("%c\t\t%s\t\t%s\t\t\t%s\n",
               quadruples[i].operator,
               quadruples[i].operand1,
               quadruples[i].operand2,
               quadruples[i].result);
    }
}

int main() {
    char expression[MAX_EXPR_LENGTH];
    int temp_count = 1; // Temporary variable count for t1, t2, ...
    Operand num_stack[MAX_EXPR_LENGTH];  // Operand stack for operands (numbers and variables)
    char op_stack[MAX_EXPR_LENGTH];  // Operator stack for operators
    int num_top = -1, op_top = -1;
    char var_name[MAX_EXPR_LENGTH];  // Variable name (for assignment)
    Quadruple quadruples[MAX_EXPR_LENGTH]; // Array to store quadruples
    int quadruple_count = 0; // Counter for quadruples

    // Get the expression from the user
    printf("Enter an arithmetic expression (e.g., c = (a + b) * (c - d)): ");
    fgets(expression, MAX_EXPR_LENGTH, stdin);

    // Look for an assignment (=) and separate the variable from the expression
    char* equals_sign = strchr(expression, '=');
    if (equals_sign != NULL) {
        // Extract variable name before '='
        strncpy(var_name, expression, equals_sign - expression);
        var_name[equals_sign - expression] = '\0';
        // Move past the '=' to start parsing the right-hand side expression
        equals_sign++;
    } else {
        printf("Invalid expression format. Missing '=' for assignment.\n");
        return 1;
    }

    // Parsing the right-hand side expression and evaluating
    for (int i = 0; i < strlen(equals_sign); i++) {
        char ch = equals_sign[i];

        // Skip spaces
        if (ch == ' ') continue;

        // If the character is a digit, form the number
        if (isdigit(ch)) {
            int num = 0;
            while (i < strlen(equals_sign) && isdigit(equals_sign[i])) {
                num = num * 10 + (equals_sign[i] - '0');
                i++;
            }
            // Push the number as a constant to the stack
            num_stack[++num_top].value = num;
            num_stack[num_top].is_variable = 0;
            i--;  // Adjust the index back to the last digit of the number
        }

        // If the character is a letter (variable name), push it onto the stack
        else if (isalpha(ch)) {
            int j = 0;
            while (i < strlen(equals_sign) && isalpha(equals_sign[i])) {
                var_name[j++] = equals_sign[i++];
            }
            var_name[j] = '\0';  // Null-terminate the variable name
            // Push the variable to the stack
            strcpy(num_stack[++num_top].name, var_name);
            num_stack[num_top].is_variable = 1;
            i--;  // Adjust the index back to the last character of the variable name
        }

        // If the character is an open parenthesis, push it to the operator stack
        else if (ch == '(') {
            op_stack[++op_top] = ch;
        }

        // If the character is a closing parenthesis, resolve the operations inside parentheses
        else if (ch == ')') {
            while (op_top >= 0 && op_stack[op_top] != '(') {
                Operand op2 = num_stack[num_top--];
                Operand op1 = num_stack[num_top--];
                char op = op_stack[op_top--];
                
                // Generate the TAC and calculate the result
                generate_TAC(op, op1, op2, temp_count);
                generate_quadruple(op, op1, op2, temp_count, quadruples, &quadruple_count);
                num_stack[++num_top].is_variable = 0;  // It's a temporary variable now
                num_stack[num_top].value = temp_count++;
            }
            // Pop the '(' from the operator stack
            op_top--;
        }

        // If the character is an operator, process it based on precedence
        else if (ch == '+' || ch == '-' || ch == '*' || ch == '/') {
            while (op_top >= 0 && precedence(op_stack[op_top]) >= precedence(ch)) {
                Operand op2 = num_stack[num_top--];
                Operand op1 = num_stack[num_top--];
                char op = op_stack[op_top--];

                // Generate the TAC and calculate the result
                generate_TAC(op, op1, op2, temp_count);
                generate_quadruple(op, op1, op2, temp_count, quadruples, &quadruple_count);
                num_stack[++num_top].is_variable = 0;  // It's a temporary variable now
                num_stack[num_top].value = temp_count++;
            }
            op_stack[++op_top] = ch;
        }
    }

    // Process any remaining operators in the stack
    while (op_top >= 0) {
        Operand op2 = num_stack[num_top--];
        Operand op1 = num_stack[num_top--];
        char op = op_stack[op_top--];

        // Generate the TAC and calculate the result
        generate_TAC(op, op1, op2, temp_count);
        generate_quadruple(op, op1, op2, temp_count, quadruples, &quadruple_count);
        num_stack[++num_top].is_variable = 0;  // It's a temporary variable now
        num_stack[num_top].value = temp_count++;
    }

    // The final result is the only element left on the stack
    printf("Final result is stored in t%d\n", num_stack[num_top].value);

    // Generate the assignment TAC for the variable
    generate_assignment_TAC(var_name, temp_count - 1);

    // Print all generated quadruples
    print_quadruples(quadruples, quadruple_count);

    return 0;
}
