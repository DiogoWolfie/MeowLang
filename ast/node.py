from abc import ABC, abstractmethod

class Node:

    def __init__(self, value, children):
        self.value = value
        self.children = children
        
    @abstractmethod
    def Evaluate(self, memory, pointer):
        pass
