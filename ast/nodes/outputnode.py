from ast.node import Node

class Output(Node):
    def __init__(self):
        super().__init__(None, [])

    def Evaluate(self, memory, pointer):
        print(chr(memory[pointer[0]]), end='')