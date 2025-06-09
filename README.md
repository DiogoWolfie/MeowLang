# MeowLang — A Felina Linguagem Minimalista

MeowLang é uma linguagem de programação minimalista inspirada em Brainfuck, mas com uma pitada de miados felinos. Criada para fins educacionais, sua estrutura é simples, porém funcional: manipula uma fita de memória e executa comandos com palavras como `meow`, `mew`, `meeow`, entre outras.

---

## EBNF da MeowLang

program       = *(instruction)

instruction   = increment
              / decrement
              / move_right
              / move_left
              / output
              / input
              / loop_start
              / loop_end
              / whitespace
              / comment

increment     = "meow"
decrement     = "mew"
move_right    = "meeow"
move_left     = "meeew"
output        = "meooooow"
input         = "mrrrow?"
loop_start    = "prrrr("
loop_end      = ")rrrpr"

whitespace    = 1*(%x20 / %x09 / %x0A / %x0D)   ; espaço, tab, newline
comment       = "#" *(%x00-0x7E)                ; ignora até o fim da linha


## Código de exemplo
meow meow meow meow meow meow meow meow meow meow  # 10
prrrr(
    meeow               # move para direita
    meow meow meow meow meow meow   # +6 = 60
    meeew               # volta para a célula da esquerda
    mew                 # decrementa
)rrrpr

meeow                  # vai para célula 1 (60)
meow meow meow meow meow   # soma 5 → total 65
meooooow               # imprime 'A'


## Requisitos
WSL
g++
flex
bison

Abra o WSL no seu terminal:
wsl -d Ubuntu

Instale os pacotes necessários (se ainda não tiver)
sudo apt update
sudo apt install build-essential flex bison

Compile o projeto
bison -d -o meowlang.tab.c parser/meowlang.y
flex -o lex.yy.c lexer/meowlang.l
g++ -o meowlang meowlang.tab.c lex.yy.c main.c ast.cpp -std=c++17

Execute o código (exemplo de entrada "input.meow")
./meowlang input.meow

Saida esperada para código de exemplo:
A

