from ast.node import Node
from collections import defaultdict

class Block(Node):
    def __init__(self, children):
        super().__init__(None, children)

    def Evaluate(self, memory=None, pointer=None):
        memory = defaultdict(int) if memory is None else memory
        pointer = [0] if pointer is None else pointer

        for child in self.children:
            child.Evaluate(memory, pointer)