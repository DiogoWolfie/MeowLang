from ast.node import Node

class Loop(Node):
    def __init__(self, children):
        super().__init__(None, children)

    def Evaluate(self, memory, pointer):
        while memory[pointer[0]] != 0:
            for child in self.children:
                child.Evaluate(memory, pointer)
