/*** Conditions ***/
%x COM DOX HYP

/*** Variables ***/
%{
    int doxFlag = 0;
%}

/*** Rules ***/
%%
 /* jednolinijkowe*/
\/\/(\/|\!)(.|\\\n)* if(doxFlag) ECHO;
\/\/(.|\\\n)* 
 /* cudzysłów */
\" BEGIN HYP; ECHO;
<HYP>\" BEGIN 0; ECHO;
<HYP>\\\" ECHO;
<HYP>\\\\ ECHO;
 /* wielolinijkowe */
<INITIAL>\/\*(\*|\!) {BEGIN DOX; yymore();}
<INITIAL>\/\* BEGIN COM;
<DOX>\*\/ {BEGIN 0; if(doxFlag) ECHO;}
<COM>\*\/ BEGIN 0;
<DOX>(.|\n)  yymore();
<COM>(.|\n)
\/\*\*\/ // /**/ - wyjątek
%%

int yywrap(){}
int main(){
    yylex();
    return 0;
}

// sprawdzenie: g++ -fpreprocessed -dD -E data/3.cpp