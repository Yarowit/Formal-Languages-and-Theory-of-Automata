/*** Variables ***/
%{
int words = 1;
int lines = 1;
%}

/*** Rules ***/
%%
[[:blank:]]*(\n[[:blank:]]*)+[^\n[:blank:]] {printf("\n%c",yytext[yyleng-1]); lines++; words++;} // kończące się znakiem
[[:blank:]]*\n[[:blank:]]*  // puste linie
[^[:blank:]\n][[:blank:]]+[^[:blank:]\n] {printf("%c %c",yytext[0],yytext[yyleng-1]); words++;}; // spacje między znakami
[[:blank:]]* // puste spacje
%%

int yywrap(){}
int main(){
    yylex();
    // printf("\nLines: %d",lines);
    // printf("\nWords: %d",words);
    return 0;
}