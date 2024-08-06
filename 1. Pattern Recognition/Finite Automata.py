# automat skończony
from sys import *

def computeTransitionFunction(pattern):
    alphabet = set(pattern)
    delta = []
    m =len(pattern)
    for q in range(m+1):
        delta.append({})
        for a in alphabet:
            k = min(m, q+1)
            while k > 0 and (pattern[:q]+a).endswith(pattern[:k]) == False :
                k -= 1
            delta[q][a] = k
    return delta

def match(file,delta):
    letter = ''
    q = 0
    m = len(delta) - 1
    i = 0
    while True:
        letter = file.read(1)
        # print(letter,end='')
        if not letter:
            break
        if letter not in delta[q]:
            q = 0
        else:
            q = delta[q][letter]
        if q == m:
            print("Wzór odnaleziony na",i-(m-1),"literze")
        i += 1


if(len(argv)) <3:
    print("Za mało argumentów")
    exit()
    
pattern = argv[1]
filename = argv[2]

file = open(filename)
delta = computeTransitionFunction(pattern)
match(file,delta)

file.close()