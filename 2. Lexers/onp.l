/*  Błędy */
%x NUM OTH ZER NEG

/*** Variables ***/
%{
    #include "stack.h"
    struct stack* s;
    char wrongSymbol;
%}

/*** Rules ***/
%%
-?[0-9]+ {
    ECHO;
    if(!s)
        s = nStack(atoi(yytext));
    else
        s = push(s,atoi(yytext));
}
 /* Operatory */
[\+\-\*\/\%\^] {
    ECHO; 
    if(!s || !s->next){
        BEGIN(NUM);
    }else{
        int b = s->v;
        s = pop(s);
        int a = s->v;
        switch(yytext[0]){
            case '+':
                s->v = a + b;
                break;
            case '*':
                s->v = a * b;
                break;
            case '-':
                s->v = a - b;
                break;
            case '/':
                if(b == 0) BEGIN ZER; // Błąd: Dzielenie przez zero
                else s->v = a / b;
                break;
            case '%':
                if(b == 0) BEGIN ZER; // Błąd: Dzielenie przez zero
                else s->v = a % b;
                break;
            case '^':
                if(b < 0) BEGIN NEG; // Błąd: Ujemna potęga
                else{
                    int acc = 1;
                    for(int i = 0; i < b; i++)
                        acc *= a;
                    s->v = acc;
                }
                break;
        }
    }
}
[[:blank:]] ECHO;
<NUM>.*\n ECHO; BEGIN 0; s = reset(s); printf("Błąd: za mała liczba argumentów\n");
<NUM>.* ECHO;
<NUM><<EOF>> printf("\nBłąd: za mała liczba argumentów\n"); return 0;
<OTH>.*\n ECHO; BEGIN 0; s = reset(s); printf("Błąd: zły znak \"%c\"\n",wrongSymbol);
<OTH>.* ECHO;
<OTH><<EOF>> printf("\nBłąd: zły znak \"%c\"\n",wrongSymbol); return 0;
<ZER>.*\n ECHO; BEGIN 0; s = reset(s); printf("Błąd: dzielenie przez zero\n");
<ZER>.* ECHO;
<ZER><<EOF>> printf("\nBłąd: dzielenie przez zero\n"); return 0;
<NEG>.*\n ECHO; BEGIN 0; s = reset(s); printf("Błąd: ujemna potęga\n");
<NEG>.* ECHO;
<NEG><<EOF>> printf("\nBłąd: ujemna potęga\n"); return 0;
\n {
    if(s){
        ECHO;
        if(s->next)
            printf("Błąd: za mała liczba operatorów\n");  
        else 
            printf(" = %d\n",s->v); 
        s = reset(s);
    }
}
<<EOF>> {
    if(s){
        if(s->next)
            printf("\nBłąd: za mała liczba operatorów\n");  
        else 
            printf("\n = %d\n",s->v); 
        s = reset(s);
    }
    return 0;
}
. ECHO; BEGIN OTH; wrongSymbol = yytext[0];
%%

int yywrap(){}
int main(){
    yylex();
    
    return 0;
}