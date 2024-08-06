from __future__ import absolute_import
from __future__ import print_function
from bison import BisonParser
# from six.moves import input
from math import gcd
def valp(a,p):
    return a % p
def neg(a,p):
    return (p-a)
def addp(a,b,p):
    return (a+b)%p
def subp(a,b,p):
    return (a-b + p)%p
def multp(a,b,p):
    return (a*b)%p
def expp(a,b,p):
    s = 1
    for i in range(b):
        s *= a
        s %= p
    return s
def inverse(a,p):
    r=0
    for i in range(1,p):
        r = (r+a)%p
        if(r==1):
            return i
    return 0
def divp(a,b,p):
    if b== 0:
        return 1
    if a==0:
        return 0
    g = gcd(a,b)
    a //= g
    b //= g
    if b==1:
        return a
    return a*inverse(b,p)%p



P=1234577
class Parser(BisonParser):
    divisionByZero = False
    divisionError = False
    """
    Implements the calculator parser. Grammar rules are defined in the method
    docstrings. Scanner rules are in the 'lexscript' attribute.
    """
    options = [
        "%define api.pure full",
        "%define api.push-pull push",
        "%lex-param {yyscan_t scanner}",
        "%parse-param {yyscan_t scanner}",
        "%define api.value.type {void *}",
    ]

    # ----------------------------------------------------------------
    # lexer tokens - these must match those in your lex script (below)
    # ----------------------------------------------------------------
    tokens = [
        'VAL',
        'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'EXP',
        'LNAW', 'PNAW',
        'NEG',
        'END', 'ERROR'
    ]
    precedences = (
        ('left', ('MINUS', 'PLUS')),
        ('left', ('TIMES', 'DIVIDE')),
        ('left', ('NEG', )),
        ('right', ('EXP', )),
    )

    start = "input"

    def on_input(self, target, option, names, values):
        """
        input : 
              | input line
        """
        # print("[[",values[0]['text'],"]]")
        return

    def on_line(self, target, option, names, values):
        """
        line : expa END
             | error END
        """
        if option == 0:
            print("[[",values[0]['text'],"]]")
            if self.divisionByZero:
                print("Dzielenie przez zero.")
            elif self.divisionError:
                print("Błąd dzielenia.")
            else:
                print("Wynik: ",values[0]['val'])
            self.divisionByZero = False
            self.divisionError = False
        if option == 1:
            print("Błąd.")
        # return values[0]
    def on_expa (self, target, option, names, values):
        """
        expa : expb  
            | expa PLUS expb
            | expa MINUS expb 
        """
        if option == 0:
            return values[0]
        if option == 1:
            return {
                'val': addp(values[0]['val'],values[2]['val'],P),
                'text': values[0]['text'] + values[2]['text'] + "+ " 
            }
        if option == 2:
            return {
                'val': subp(values[0]['val'],values[2]['val'],P),
                'text': values[0]['text'] + values[2]['text'] + "- " 
            }
    
    def on_expb(self, target, option, names, values):
        """
        expb : expc  
             | expb TIMES expc
             | expb DIVIDE expc 
        """
        if option == 0:
            return values[0]
        if option == 1:
            return {
                'val': multp(values[0]['val'],values[2]['val'],P),
                'text': values[0]['text'] + values[2]['text'] + "* " 
            }
        if option == 2:
            if values[2]['val'] == 0:
                self.divisionByZero = True
            return {
                'val': divp(values[0]['val'],values[2]['val'],P),
                'text': values[0]['text'] + values[2]['text'] + "/ " 
            }
    def on_expc(self, target, option, names, values):
        """
        expc : expd  
             | expd EXP powc
        """
        if option == 0:
            return values[0]
        if option == 1:
            val = {
                'text': values[0]['text'] + values[2]['text'] + "^ "
            }
            if 'isUndefined' in values[0] and values[0]['isUndefined'] == True:
                res = divp(values[0]['numer']*values[2]['val'],values[0]['denom'],P-1)
                
                if res == 0:
                    self.divisionError = True
                    val['val'] = 1
                    val['denom'] = values[2]['val']
                    val['numer'] = multp(values[0]['numer'],values[2]['val'],P-1)
                else:
                    val['val'] = expp(values[0]['base'],res,P)
                    self.divisionError = False
            elif 'isUndefined' in values[2] and values[2]['isUndefined'] == True:
                val['isUndefined'] = True
                val['base'] = values[0]['val']
                val['denom'] = values[2]['denom']
                val['numer'] = values[2]['numer']
                val['val'] = 1
            else:
                val['isUndefined'] = False
                val['val'] = expp(values[0]['val'],values[2]['val'],P)
            
            return val
    def on_expd(self, target, option, names, values):
        """
        expd : expe  
             | VAL
        """
        if option == 0:
            return values[0]
        if option == 1:
            return {
                'val': valp(int(values[0]),P),
                'text': str(valp(int(values[0]),P)) + " ",
                'isUndefined': False
            }
    def on_expe(self, target, option, names, values):
        """
        expe : NEG VAL  
             | NEG expe
             | LNAW expa PNAW
        """
        if option == 0:
            return {
                'val': neg(valp(int(values[1]),P),P),
                'text': str(neg(valp(int(values[1]),P),P)) + " ",
                'isUndefined': False
            }
        if option == 1:
            return {
                'val': neg(values[1]['val'],P),
                'text': " -" + values[1]['text'],
                'isUndefined': False
            }
        if option == 2:
            return values[1]
    
    def on_powa(self, target, option, names, values):
        """
        powa : powb  
             | powa PLUS powb
             | powa MINUS powb 
        """
        if option == 0:
            return values[0]
        if option == 1:
            return {
                'val': addp(values[0]['val'],values[2]['val'],P-1),
                'text': values[0]['text'] + values[2]['text'] + "+ " 
            }
        if option == 2:
            return {
                'val': subp(values[0]['val'],values[2]['val'],P-1),
                'text': values[0]['text'] + values[2]['text'] + "- " 
            }
    def on_powb(self, target, option, names, values):
        """
        powb : powc
             | powb TIMES powc
             | powb DIVIDE powc 
        """
        if option == 0:
            return values[0]
        if option == 1:
            return {
                'val': multp(values[0]['val'],values[2]['val'],P-1),
                'text': values[0]['text'] + values[2]['text'] + "* " 
            }
        if option == 2:
            val = {'text': values[0]['text'] + values[2]['text'] + "/ " 
            }
            if values[2]['val'] == 0:
                self.divisionByZero = True
                val['val'] = 1
            else:
                res = divp(values[0]['val'],values[2]['val'],P-1)
                if values[0]['val'] != 0 and res == 0:
                    # global divisionError
                    self.divisionError = True
                    val['val'] = 1
                    val['isUndefined'] = True
                    val['denom'] = values[2]['val']
                    val['numer'] = values[0]['val']
                else:
                    val['isUndefined'] = False
                    val['val'] = divp(values[0]['val'],values[2]['val'],P-1)
           
            return val
    def on_powc(self, target, option, names, values):
        """
        powc : powd
             | VAL
        """
        if option == 0:
            return values[0]
        if option == 1:
            return {
                'val': valp(int(values[0]),P-1),
                'text': str(valp(int(values[0]),P-1)) + " ",
                'isUndefined': False
            }
    def on_powd(self, target, option, names, values):
        """
        powd : NEG VAL  
             | NEG powd
             | LNAW powa PNAW
        """
        if option == 0:
            return {
                'val': neg(valp(int(values[1]),P-1),P-1),
                'text': str(neg(valp(int(values[1]),P-1),P-1)) + " ",
                'isUndefined': False
            }
        if option == 1:
            return {
                'val': neg(values[1]['val'],P-1),
                'text': " -" + values[1]['text'],
                'isUndefined': False
            }
        if option == 2:
            return values[1]
        
    lexscript = r"""
    %option noyywrap
    %option yylineno
    %x OPE
    %option reentrant bison-bridge bison-locations
    %{
    #include "Python.h"
    #include "tmp.tab.h"
    extern void *py_parser;
    extern void (*py_input)(PyObject *parser, char *buf, int *result, int max_size);
    PyMODINIT_FUNC PyInit_Parser(void) { /* windows needs this function */ }
    #define returntoken(tok) \
            *yylval = (void*)PyUnicode_FromString(strdup(yytext)); return (tok);
    #define YY_INPUT(buf,result,max_size) { \
        (*py_input)(py_parser, buf, &result, max_size); \
    }
    %}

    num [0-9]*


    %%
    .#.*\n returntoken(ERROR);
    \#.*\n 
    <INITIAL,OPE>\\\n
    <INITIAL,OPE>[ \t]+ 	;
    <INITIAL,OPE>{num} { BEGIN OPE; returntoken(VAL); }
    <INITIAL>\- returntoken(NEG);

    <OPE>\*	{ BEGIN INITIAL; returntoken(TIMES); }
    <OPE>\-	{ BEGIN INITIAL; returntoken(MINUS); }
    <OPE>\+	{ BEGIN INITIAL; returntoken(PLUS); }
    <OPE>\/	{ BEGIN INITIAL; returntoken(DIVIDE); }
    <OPE>\^	{ BEGIN INITIAL; returntoken(EXP); }
    <INITIAL>\(	{ returntoken(LNAW);}
    <OPE>\)	{ returntoken(PNAW); }
    <INITIAL,OPE>\n	{ BEGIN INITIAL; returntoken(END); }
    <INITIAL,OPE>.	{ returntoken(ERROR); }
    %%
    """
if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(prog="PyBison CALC Example")
    parser.add_argument("-k", "--keepfiles", action="store_true",
                        help="Keep temporary files used in building parse engine lib")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Enable verbose messages while parser is running")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Enable garrulous debug messages from parser engine")
    args = parser.parse_args()

    p = Parser(keepfiles=args.keepfiles, verbose=args.verbose)

    while True:
        try:
            s = input()+'\n'
            r = p.parse_string(s, debug=args.debug)
            
            # if p.errorEncountered:
            #     print("Błąd")
            # else:
            #     print("[[",r['text'],"]]")
            #     if p.divisionByZero:
            #         print("Dzielenie przez zero.")
            #     elif p.divisionError:
            #         print("Błąd dzielenia.")
            #     else:
            #         print("Wynik: ",r['val'])
            # p.divisionByZero = False
            # p.divisionError = False
            # p.errorEncountered = False
        
            # print(r)
        except (KeyboardInterrupt, EOFError):
            break