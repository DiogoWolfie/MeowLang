#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <map>
#include "ast/ast.h"

extern int yyparse();
extern FILE* yyin;
extern Block* root;

// Pré-processamento: remove comentários '#' e salva em novo arquivo
void preprocess_and_save(const char* input_path, const char* output_path) {
    FILE* in = fopen(input_path, "r");
    FILE* out = fopen(output_path, "w");

    if (!in || !out) {
        perror("Erro ao abrir arquivos para pré-processamento");
        exit(1);
    }

    char line[1024];
    while (fgets(line, sizeof(line), in)) {
        char* comment = strchr(line, '#');
        if (comment) *comment = '\0';  // Trunca no '#'

        // Garante que termina com \n
        size_t len = strlen(line);
        if (len == 0 || line[len - 1] != '\n') {
            strcat(line, "\n");
        }

        fputs(line, out);
    }

    fclose(in);
    fclose(out);
}

int main(int argc, char** argv) {
    if (argc < 2) {
        printf("Uso: ./meowlang <arquivo.meow>\n");
        return 1;
    }

    preprocess_and_save(argv[1], "clean_input.meow");

    FILE* input = fopen("clean_input.meow", "r");
    if (!input) {
        perror("Erro ao abrir clean_input.meow");
        return 1;
    }

    yyin = input;

    if (yyparse() == 0) {
        std::map<int, int> memory;
        int pointer = 0;
        root->Evaluate(memory, &pointer);
    }

    fclose(input);
    return 0;
}
