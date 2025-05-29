from lexer.token import Token

#análise léxica
class Tokenizer:

    def __init__(self, source):
        self.source = source #código fonte
        self.position = 0 #posição atual que o tokenizer está separando
        self.next = None #o último token separado
        self.selectNext()



    def selectNext(self):
        
        palavras_reservadas = ["meow", "mew", "meeow", "meeew", "meooooow", "mrrrow?", "prrrr(", ")rrrpr"]

        #ignora todos os espaços em branco
        while self.position < len(self.source) and self.source[self.position] in [' ', '\t', "\n"]:
            self.position += 1 
    
        if self.position >= len(self.source):
            self.next = Token("EOF", None)
            return

        current_char = self.source[self.position]

        if current_char.isalpha() or current_char in ['(', ')', '?']:
            identifier = ''
            while self.position < len(self.source) and self.source[self.position] not in [' ', '\t', '\n']:
                identifier += self.source[self.position]
                self.position += 1

            if identifier in palavras_reservadas:
                if identifier == "meow":
                    self.next = Token("increment", identifier)
                    return
                
                elif identifier == "mew":
                    self.next = Token("decrement", identifier)
                    return
                
                elif identifier == "meeow":
                    self.next = Token("move_right", identifier)
                    return
                
                elif identifier == "meeew":
                    self.next = Token("move_left", identifier)
                    return
                
                elif identifier == "meooooow":
                    self.next = Token("output", identifier)
                    return
                
                elif identifier == "mrrrow?":
                    self.next = Token("input", identifier)
                    return
                
                elif identifier == "prrrr(":
                    self.next = Token("loop_start", identifier)
                    return
                
                elif identifier == ")rrrpr":
                    self.next = Token("loop_end", identifier)
                    return
                
        # token não reconhecido
        raise Exception(f"Token inválido na posição {self.position}: '{self.source[self.position:]}'")