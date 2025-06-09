#include "ast/ast.h"
#include <iostream>

// Block
void Block::Evaluate(Memory& memory, int* pointer) {
    for (auto child : children) {
        child->Evaluate(memory, pointer);
    }
}

// Increment
void Increment::Evaluate(Memory& memory, int* pointer) {
    memory[*pointer]++;
}

// Decrement
void Decrement::Evaluate(Memory& memory, int* pointer) {
    memory[*pointer]--;
}

// MoveRight
void MoveRight::Evaluate(Memory& memory, int* pointer) {
    (*pointer)++;
}

// MoveLeft
void MoveLeft::Evaluate(Memory& memory, int* pointer) {
    if (*pointer > 0) (*pointer)--;
}

// Output
void Output::Evaluate(Memory& memory, int* pointer) {
    std::cout << static_cast<char>(memory[*pointer]) << std::endl;
}

// Input
void Input::Evaluate(Memory& memory, int* pointer) {
    char ch;
    std::cin >> ch;
    memory[*pointer] = static_cast<int>(ch);
}

// Loop
void Loop::Evaluate(Memory& memory, int* pointer) {
    while (memory[*pointer] != 0) {
        for (auto child : children) {
            child->Evaluate(memory, pointer);
        }
    }
}
