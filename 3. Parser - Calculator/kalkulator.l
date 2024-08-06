%option noyywrap
%option yylineno
%x OPE


%{
#include "kalkulator_y.h"
int yylex();
%}

num [0-9]*


%%
^#.*\n
<INITIAL,OPE>\\\n
<INITIAL,OPE>[ \t]+ 	;
<INITIAL,OPE>{num} { yylval.v = atoi(yytext); BEGIN OPE; return VAL; }
<INITIAL>\- return NEG;

<OPE>\*	{ BEGIN INITIAL; return TIMES; }
<OPE>\-	{ BEGIN INITIAL; return MINUS; }
<OPE>\+	{ BEGIN INITIAL; return PLUS; }
<OPE>\/	{ BEGIN INITIAL; return DIVIDE; }
<OPE>\^	{ BEGIN INITIAL; return EXP; }
<INITIAL>\(	{ return LNAW;}
<OPE>\)	{ return PNAW; }
<INITIAL,OPE>\n	{ BEGIN INITIAL; return END; }
<INITIAL,OPE>.	{ return ERROR; }
%%