from ast.node import Node

class MoveRight(Node):
    def __init__(self):
        super().__init__(None, [])

    def Evaluate(self, memory, pointer):
        pointer[0] += 1
        if pointer[0] >= len(memory):
            memory.append(0)
