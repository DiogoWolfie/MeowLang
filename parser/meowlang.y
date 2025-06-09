%{
#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include "ast/ast.h"

Block* root;
int yylex();
int yyerror(const char* s);
%}

%union {
    void* node;
    void* nodelist;
}

%token INCREMENT DECREMENT MOVERIGHT MOVELEFT OUTPUT INPUT LOOPSTART LOOPEND
%type <node> instruction
%type <nodelist> program instructions loop_body

%%

program:
    instructions {
        root = new Block(*(std::vector<Node*>*)$1);
        delete (std::vector<Node*>*)$1;
    }
;

instructions:
    /* vazio */ {
        $$ = (void*) new std::vector<Node*>();
    }
  | instructions instruction {
        auto list = (std::vector<Node*>*) $1;
        list->push_back((Node*) $2);
        $$ = (void*) list;
    }
;

instruction:
    INCREMENT              { $$ = (void*) new Increment(); }
  | DECREMENT              { $$ = (void*) new Decrement(); }
  | MOVERIGHT              { $$ = (void*) new MoveRight(); }
  | MOVELEFT               { $$ = (void*) new MoveLeft(); }
  | OUTPUT                 { $$ = (void*) new Output(); }
  | INPUT                  { $$ = (void*) new Input(); }
  | LOOPSTART loop_body LOOPEND {
        $$ = (void*) new Loop(*(std::vector<Node*>*)$2);
        delete (std::vector<Node*>*)$2;
    }
;

loop_body:
    instructions {
        $$ = $1;
    }
;

%%

int yyerror(const char *s) {
    fprintf(stderr, "Erro de sintaxe: %s\n", s);
    return 1;
}
