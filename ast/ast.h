#ifndef AST_H
#define AST_H

#include <vector>
#include <map>

// Ponteiro para célula atual
typedef std::map<int, int> Memory;

class Node {
public:
    virtual void Evaluate(Memory& memory, int* pointer) = 0;
    virtual ~Node() = default;
};

class Block : public Node {
    std::vector<Node*> children;
public:
    Block(std::vector<Node*> children) : children(children) {}
    void Evaluate(Memory& memory, int* pointer) override;
};

// Aqui você declara os outros nós (Increment, Decrement, etc.) também
class Increment : public Node {
public:
    void Evaluate(Memory& memory, int* pointer) override;
};

class Decrement : public Node {
public:
    void Evaluate(Memory& memory, int* pointer) override;
};

class MoveRight : public Node {
public:
    void Evaluate(Memory& memory, int* pointer) override;
};

class MoveLeft : public Node {
public:
    void Evaluate(Memory& memory, int* pointer) override;
};

class Output : public Node {
public:
    void Evaluate(Memory& memory, int* pointer) override;
};

class Input : public Node {
public:
    void Evaluate(Memory& memory, int* pointer) override;
};

class Loop : public Node {
    std::vector<Node*> children;
public:
    Loop(std::vector<Node*> children) : children(children) {}
    void Evaluate(Memory& memory, int* pointer) override;
};

#endif
