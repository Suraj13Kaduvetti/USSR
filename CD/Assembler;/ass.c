#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define MAX_INSTRUCTIONS 100
#define MAX_SYMBOLS 50
#define MAX_OPCODES 20

// Struct to hold symbol table entries
typedef struct {
    char symbol[20];
    int address;
    int defined;
    int used;
} Symbol;

// Struct to hold the opcode table entries
typedef struct {
    char mnemonic[10];
    int machine_code;
} Opcode;

// Symbol and Opcode tables
Symbol symtab[MAX_SYMBOLS];
Opcode optab[MAX_OPCODES];

// Assembly code input and output
char assembly_code[MAX_INSTRUCTIONS][100];
int num_instructions = 0;
int current_location = 1000;  // Default starting location

// Function to initialize the opcode table with custom values
void init_optab() {
    // Extended set of opcode entries
    strcpy(optab[0].mnemonic, "MOV");
    optab[0].machine_code = 0x10;
    
    strcpy(optab[1].mnemonic, "ADD");
    optab[1].machine_code = 0x20;
    
    strcpy(optab[2].mnemonic, "SUB");
    optab[2].machine_code = 0x30;

    strcpy(optab[3].mnemonic, "JMP");
    optab[3].machine_code = 0x40;

    strcpy(optab[4].mnemonic, "INP");
    optab[4].machine_code = 0x50;
    
    strcpy(optab[5].mnemonic, "STO");
    optab[5].machine_code = 0x60;
    
    strcpy(optab[6].mnemonic, "OUT");
    optab[6].machine_code = 0x70;
    
    strcpy(optab[7].mnemonic, "HLT");
    optab[7].machine_code = 0x80;
    
    strcpy(optab[8].mnemonic, "DS");
    optab[8].machine_code = 0x90; // Custom opcode for DS (define space)
    strcpy(optab[9].mnemonic, "START");
    optab[9].machine_code = -1;  // Custom handling for START mnemonic (no machine code)
}

// Function to search for an opcode in the opcode table
int search_optab(char *mnemonic) {
    for (int i = 0; i < MAX_OPCODES; i++) {
        if (strcmp(optab[i].mnemonic, mnemonic) == 0) {
            return optab[i].machine_code;
        }
    }
    return -1;  // Opcode not found
}

// Function to add a symbol to the symbol table
int add_symbol(char *symbol, int address) {
    for (int i = 0; i < MAX_SYMBOLS; i++) {
        if (symtab[i].symbol[0] == '\0') {  // Empty slot found
            strcpy(symtab[i].symbol, symbol);
            symtab[i].address = address;
            symtab[i].defined = 1;
            symtab[i].used = 0;
            return 1;
        }
    }
    return 0;  // Symbol table full
}

// Function to print the symbol table
void print_symtab() {
    printf("Symbol Table:\n");
    printf("Symbol | Address | Defined | Used\n");
    for (int i = 0; i < MAX_SYMBOLS; i++) {
        if (symtab[i].symbol[0] != '\0') {
            printf("%s\t%d\t%d\t%d\n", symtab[i].symbol, symtab[i].address, symtab[i].defined, symtab[i].used);
        }
    }
}

// Function to display the opcode table
void print_optab() {
    printf("Opcode Table:\n");
    printf("Mnemonic | Machine Code\n");
    for (int i = 0; i < MAX_OPCODES; i++) {
        if (optab[i].mnemonic[0] != '\0') {
            printf("%s\t0x%X\n", optab[i].mnemonic, optab[i].machine_code);
        }
    }
}

// Function to parse an assembly instruction
void parse_instruction(char *line, int location) {
    char mnemonic[10], operand[20];
    int machine_code;

    // Extract the mnemonic and operand (simplified)
    sscanf(line, "%s %s", mnemonic, operand);

    // Handle the START mnemonic
    if (strcmp(mnemonic, "START") == 0) {
        if (strlen(operand) > 0) {
            current_location = atoi(operand);  // Set the starting address to the operand value
        } else {
            printf("Error: Missing address for START mnemonic.\n");
        }
        return;
    }

    // Search for the mnemonic in the opcode table
    machine_code = search_optab(mnemonic);
    if (machine_code == -1) {
        printf("Error: Invalid mnemonic %s at location %d\n", mnemonic, location);
        return;
    }

    // Handle operand (simple example, no real operand handling here)
    if (strlen(operand) > 0 && strcmp(mnemonic, "DS") != 0) {
        // For simplicity, assume operand is a symbol
        add_symbol(operand, location + 1);  // Assume symbol address is next line
    }

    // Print the machine code for the instruction
    printf("Location %d: %s %s --> Machine Code: 0x%X\n", location, mnemonic, operand, machine_code);
}

// Main program function
int main() {
    char line[100];
    
    // Initialize opcode table
    init_optab();

    // Sample assembly program input
    printf("Enter the assembly program (type 'END' to finish):\n");
    while (1) {
        printf("Enter instruction: ");
        fgets(line, sizeof(line), stdin);
        line[strcspn(line, "\n")] = 0;  // Remove newline character

        if (strcmp(line, "END") == 0) {
            break;
        }

        strcpy(assembly_code[num_instructions], line);
        num_instructions++;
    }

    // Parse and process the assembly program
    printf("\nProcessing Assembly Program:\n");
    for (int i = 0; i < num_instructions; i++) {
        parse_instruction(assembly_code[i], current_location);
        current_location += 4;  // Assume each instruction takes 4 bytes
    }

    // Display symbol table and opcode table
    print_symtab();
    print_optab();

    return 0;
}
