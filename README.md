# MeowLang

; Programa é uma sequência de instruções válidas
program       = *(instruction)

; Instruções são compostas por comandos únicos
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
comment       = "#" *(%x00-0x7E)                ; ignora comentário até fim da linha
