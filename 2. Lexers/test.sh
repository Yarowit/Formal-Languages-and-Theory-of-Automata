#!/bin/bash

lex whitespace.l
gcc lex.yy.c
./a.out < data/1.a > out/1.a
./a.out < data/1.b > out/1.b
cmp out/1.a check/1.a
cmp out/1.b check/1.b
echo Testy zaliczone