from ast.node import Node

class Block(Node):
    def __init__(self, children):
        super().__init__(None, children)

    def Evaluate(self, memory=None, pointer=None):
        memory = [0] * 30000 if memory is None else memory
        pointer = [0] if pointer is None else pointer

        for child in self.children:
            child.Evaluate(memory, pointer)