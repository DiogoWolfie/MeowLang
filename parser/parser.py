from lexer.tokenizer import Tokenizer
from ast.nodes.inputnode import Input
from ast.nodes.outputnode import Output
from ast.nodes.loopnode import Loop
from ast.nodes.mrnode import MoveRight
from ast.nodes.mlnode import MoveLeft
from ast.nodes.incnode import Increment
from ast.nodes.decnode import Decrement

#anáçise sintática
class Parser:
    tokenizer = None

    
    @staticmethod
    def parseStatement():
        token = Parser.tokenizer.next

        if token.type == "increment":
            Parser.tokenizer.selectNext()
            return Increment()

        elif token.type == "decrement":
            Parser.tokenizer.selectNext()
            return Decrement()

        elif token.type == "move_right":
            Parser.tokenizer.selectNext()
            return MoveRight()

        elif token.type == "move_left":
            Parser.tokenizer.selectNext()
            return MoveLeft()

        elif token.type == "output":
            Parser.tokenizer.selectNext()
            return Output()

        elif token.type == "input":
            Parser.tokenizer.selectNext()
            return Input()

        elif token.type == "loop_start":
            Parser.tokenizer.selectNext()  # consome 'prrrr('
            body = []
            while Parser.tokenizer.next.type != "loop_end":
                body.append(Parser.parseStatement())
            Parser.tokenizer.selectNext()  # consome ')rrrpr'
            return Loop(body)

        else:
            raise ValueError(f"Token inesperado: {token.type}")

    @staticmethod
    def run(source):
        Parser.tokenizer = Tokenizer(source)
        children = []

        while Parser.tokenizer.next.type != "EOF":
            children.append(Parser.parseStatement())

        from ast.nodes.blocknode import Block
        return Block(children)

