from ast.node import Node

class MoveLeft(Node):
    def __init__(self):
        super().__init__(None, [])

    def Evaluate(self, memory, pointer):
        if pointer[0] > 0:
            pointer[0] -= 1
