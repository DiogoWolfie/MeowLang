from ast.node import Node

class Increment(Node):
    def __init__(self):
        super().__init__(None, [])

    def Evaluate(self, memory, pointer):
        memory[pointer[0]] += 1
