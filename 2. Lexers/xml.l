/*** Conditions ***/
%x HYP CDATA COM
/*** Variables ***/
%{
%}
/*** Rules ***/
%%
\" ECHO; BEGIN HYP;
<HYP>\" ECHO; BEGIN 0;

\<!\[CDATA\[ ECHO; BEGIN CDATA;
<CDATA>\]\]\> ECHO; BEGIN 0; // Cdata

\<!-- BEGIN COM; yymore();
<COM>(.|\n) yymore();
<COM>--\> {
    // invalid przez --
    for(int i=3; i< yyleng-3; i++){
        if(yytext[i] == yytext[i+1] && yytext[i] == '-'){
            ECHO;
            break;
        }
    }
    BEGIN 0;
}
%%

int yywrap(){}
int main(){
    yylex();
    return 0;
}