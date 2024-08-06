#!/bin/bash

lex $1
gcc lex.yy.c
./a.out < $2