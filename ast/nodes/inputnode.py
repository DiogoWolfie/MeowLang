from ast.node import Node

class Input(Node):
    def __init__(self):
        super().__init__(None, [])

    def Evaluate(self, memory, pointer):
        entrada = input()[0]
        memory[pointer[0]] = ord(entrada)
