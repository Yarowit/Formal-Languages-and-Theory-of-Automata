#include <stdio.h>
#include <string.h>
#include <stdlib.h>

const int p = 1234577;

// konkatenacja

char* two(char* one, char* two){
    char* newChar;
    newChar = (char*)malloc(strlen(one)+strlen(two)); 
    strcpy(newChar, one); 
    strcat(newChar, two); 

    return newChar;
}

char* three(char* one, char* two, char* three){
    char* newChar;
    newChar = (char*)malloc(strlen(one)+strlen(two)+strlen(three)); 
    strcpy(newChar, one); 
    strcat(newChar, two); 
    strcat(newChar, three); 

    return newChar;
}

char* toString(int x){
    int length = snprintf( NULL, 0, "%d", x );
    char* str = (char*)malloc( length + 1 );
    snprintf( str, length + 1, "%d", x );

    return str;
}

inline int valp(int a, int p){
    return a % p;
}
inline int neg(int a, int p){
    return (p - a);
}
inline int addp(int a, int b, int p){
    return (a + b) % p;
}
inline int subp(int a, int b, int p){
    return (a - b + p) % p;
}
inline int multp(int a, int b, int p){
    return (a * b) % p;
}

int expp(int a, int b, int p){
    ulong s = 1;
    for(int i=0; i<b; i++){
        s *= a;
        s %= p;
    }
    return (int)s;
}

int inverse(int a, int p){
    int r = 0;
    for(int i=1; i<p; i++){
        r = (r+a) % p;
        if(r == 1)
            return i;
    }
    return 0;
}


int gcd(int a, int b){ 
    int result = ((a < b) ? a : b); 
    while (result > 0) { 
        if (a % result == 0 && b % result == 0)
            break; 
        result--; 
    } 
    
    return result; 
} 

int divp(int a, int b, int p){
    if(a == 0) return 0;

    int g = gcd(a,b);
    a /= g;
    b /= g;

    if(b == 1) return a;
    
    return (int)((long)a * (long)inverse(b,p) % (long)p);
}

