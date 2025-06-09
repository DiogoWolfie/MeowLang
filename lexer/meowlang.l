%{
#include "meowlang.tab.h"
%}

%%
meow         { return INCREMENT; }
mew          { return DECREMENT; }
meeow        { return MOVERIGHT; }
meeew        { return MOVELEFT; }
meooooow     { return OUTPUT; }
mrrrow\?     { return INPUT; }
prrrr\(      { return LOOPSTART; }
\)rrrpr      { return LOOPEND; }

[ \t\r\n]+    { /* ignora espaços, tabs e quebras de linha */ }
"#".*         { /* ignora comentários */ }

[a-zA-Z\?\(\)]+ {
    printf("Token desconhecido: %s\n", yytext);
    return -1;
}
%%

int yywrap() {
    return 1;
}
