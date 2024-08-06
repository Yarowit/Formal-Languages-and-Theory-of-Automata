# Knuth Morris Pratt
from sys import *

def computePi(pattern):
    pi = [-1]
    k = -1 # -1 oznacza brak dopasowania
    for q in range(1, len(pattern)):
        while k >= 0 and pattern[k+1] != pattern[q]:
            k = pi[k]
        if pattern[k+1] == pattern[q]:
            k += 1
        pi.append(k)
    return pi

def KMP(file, pattern):
    letter = ''
    m = len(pattern)
    pi = computePi(pattern)
    q = -1
    i = 0
    while True:
        letter = file.read(1)
        # print(letter,end='')
        if not letter:
            break

        while q >= 0 and pattern[q+1] != letter:
            q = pi[q]
        if pattern[q+1] == letter:
            q += 1
        if q == m-1:
            print("Wzór odnaleziony na",i-(m-1),"literze")
            q = pi[q]
        i += 1


if(len(argv)) <3:
    print("Za mało argumentów")
    exit()
    
pattern = argv[1]
filename = argv[2]

# pattern = "bcab"
# filename = "1.txt"

file = open(filename)

KMP(file, pattern)

file.close()