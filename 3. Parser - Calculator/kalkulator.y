%union {
    struct{
        int val;
        int isUndefined;
        int base;
        int numer;
        int denom;
        char * text;
    } d;
    int v;
}

%{
#include <stdbool.h>
#include "lib/operacje.h"
extern int yytext;  // z lex-a
int yylex();
int yyerror(char*);

int divisionByZero = false;
int divisionError = false;

%}

%token <v> VAL
%token TIMES
%token PLUS
%token MINUS
%token DIVIDE
%token EXP
%token NEG
%token LNAW
%token PNAW
%token END
%token ERROR


%type <d> input
%type <d> exp1
%type <d> exp2
%type <d> exp3
%type <d> exp4
%type <d> exp5
%type <d> exp1exp
%type <d> exp2exp
%type <d> exp3exp
%type <d> exp4exp

%%
input: {} 
    | input line
;
line:  exp1 END { printf("[[ %s ]]\n",$1.text);
                  if(divisionByZero) printf("Dzielenie przez zero.\n");
                  else if(divisionError) printf("Błąd dzielenia.\n");
                  else printf("Wynik:  %d\n",$1.val); 
                  divisionByZero = false; 
                  divisionError = false;
                 }
    | error END {printf("Błąd.\n");}

exp1: exp2  {$$ = $1;}
    | exp1 PLUS exp2 { $$.val = addp($1.val, $3.val, p);
                        $$.text = three($1.text, $3.text, "+ "); }
    | exp1 MINUS exp2 { $$.val = subp($1.val, $3.val, p); 
                        $$.text = three($1.text, $3.text, "- "); }
    
exp2: exp3  {$$ = $1;}   
    | exp2 TIMES exp3 { $$.val = multp($1.val, $3.val, p);
                        $$.text = three($1.text, $3.text, "* "); }
    | exp2 DIVIDE exp3 {if($3.val == 0){ divisionByZero = true; $$.val = 1;}
                        else $$.val = divp($1.val, $3.val, p);
                        $$.text = three($1.text, $3.text, "/ "); }
exp3: exp4  {$$ = $1;}   
    | exp4 EXP exp3exp {   if($1.isUndefined){
                                int res = divp(($1.numer * $3.val), $1.denom, p - 1);
                                
                                if(res == 0){
                                    divisionError = true;
                                    $$.val = 1;
                                    $$.denom = $3.val;
                                    $$.numer = multp($1.numer,$3.val,p-1);
                                }else{
                                    $$.val = expp($1.base,res,p);
                                    divisionError = false;
                                }
                            }else if($3.isUndefined){
                                $$.isUndefined = true;
                                $$.base = $1.val;
                                $$.denom = $3.denom;
                                $$.numer = $3.numer;
                            }else{
                                $$.isUndefined = false;
                                $$.val = expp($1.val,$3.val,p);
                            }
                            $$.text = three($1.text, $3.text, "^ ");
                        }
    
exp4: exp5 {$$ = $1;}
    | VAL  {$$.val = valp($1, p);$$.isUndefined=false;  $$.text = three("",toString(valp($1, p))," "); }

exp5: NEG VAL {$$.val = neg($2, p);  $$.text = two(toString(neg($2, p)), " "); }                       
    | NEG exp5 {$$.val = neg($2.val, p);  $$.text = two(" -",$2.text); }                       
    | LNAW exp1 PNAW { $$ = $2; }


// potęga ~ p-1

exp1exp: exp2exp  {$$ = $1;}
        | exp1exp PLUS exp2exp { $$.val = addp($1.val, $3.val, p - 1);
                        $$.text = three($1.text, $3.text, "+ "); }
        | exp1exp MINUS exp2exp { $$.val = subp($1.val, $3.val, p - 1); 
                        $$.text = three($1.text, $3.text, "- "); }
    
exp2exp: exp3exp  {$$ = $1;}   
        | exp2exp TIMES exp3exp { $$.val = multp($1.val, $3.val, p - 1);
                        $$.text = three($1.text, $3.text, "* "); }
        | exp2exp DIVIDE exp3exp {
                        if($3.val == 0){
                            divisionByZero = true;
                            $$.val = 1;
                        }else{ 
                            int res = divp($1.val, $3.val, p - 1);
                            if($1.val != 0 && res == 0){
                                divisionError = true;
                                $$.val = 1;
                                $$.isUndefined = true;
                                $$.denom = $3.val;
                                $$.numer = $1.val;
                            }else{
                                $$.isUndefined = false;
                                $$.val = divp($1.val, $3.val, p - 1);
                            }
                        }
                        $$.text = three($1.text, $3.text, "/ "); }
    
exp3exp: exp4exp {$$ = $1;}
        | VAL  {$$.val = valp($1, p - 1);  $$.text = three("",toString(valp($1, p - 1))," "); }

exp4exp: NEG VAL {$$.val = neg($2, p - 1);  $$.text = two(toString(neg($2, p - 1)), " "); }                       
        | NEG exp4exp {$$.val = neg($2.val, p - 1);  $$.text = two(" -",$2.text); }                       
        | LNAW exp1exp PNAW { $$ = $2; }
;

%%
int yyerror(char *s)
{
    return 0;
}

int main()
{
    yyparse();
    return 0;
}
