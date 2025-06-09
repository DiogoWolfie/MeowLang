# 🐾 MeowLang — A Felina Linguagem Minimalista

MeowLang é uma linguagem de programação minimalista inspirada em **Brainfuck**, mas com uma pitada de miados felinos. Criada para fins educacionais, sua estrutura é simples, porém funcional: manipula uma fita de memória e executa comandos com palavras como `meow`, `mew`, `meeow`, entre outras.

---

## 📜 EBNF da MeowLang

```ebnf
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
```

---

## 🐱‍💻 Comandos

| Comando      | Símbolo         | Descrição                        |
|--------------|-----------------|----------------------------------|
| Incrementar  | `meow`          | Soma 1 à célula atual            |
| Decrementar  | `mew`           | Subtrai 1 da célula atual        |
| Direita      | `meeow`         | Move para a célula à direita     |
| Esquerda     | `meeew`         | Move para a célula à esquerda    |
| Saída        | `meooooow`      | Imprime caractere da célula      |
| Entrada      | `mrrrow?`       | Lê caractere para a célula       |
| Início Loop  | `prrrr(`        | Início de um loop                |
| Fim Loop     | `)rrrpr`        | Fim de um loop                   |
| Comentário   | `# ...`         | Ignora até o fim da linha        |
| Espaço/Tab   |                 | Ignorado                         |

---

## ✨ Exemplo de Código

```meowlang
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
```

Saída esperada:
```
A
```

---

## ⚙️ Requisitos

- **WSL**
- **g++**
- **flex**
- **bison**

---

## 🚀 Como Compilar e Executar

1. **Abra o WSL no seu terminal:**
   ```sh
   wsl -d Ubuntu
   ```

2. **Instale os pacotes necessários (se ainda não tiver):**
   ```sh
   sudo apt update
   sudo apt install build-essential flex bison
   ```

3. **Compile o projeto:**
   ```sh
   bison -d -o meowlang.tab.c parser/meowlang.y
   flex -o lex.yy.c lexer/meowlang.l
   g++ -o meowlang meowlang.tab.c lex.yy.c main.c ast.cpp -std=c++17
   ```

4. **Execute o código (exemplo de entrada "input.meow"):**
   ```sh
   ./meowlang input.meow
   ```

---

## 😺 Divirta-se programando com miados!