'''
CSES Problem Set 
Introductory Problems - Permutations

# Author        : Sunkeerth M
# Description   : A permutation of integers 1,2,…,n is called beautiful if there are no 
                  adjacent elements whose difference is 1. Given n, construct a beautiful
                  permutation if such a permutation exists. Input - The only input line 
                  contains an integer n. Output - Print a beautiful permutation of integers 
                  1,2,…,n. If there are several solutions, you may print any of them. 
                  If there are no solutions, print "NO SOLUTION".

# Date          : 19-07-2020

'''

from itertools import permutations

def isEven(n) : 
    return (n & 1);

input_n = int(input())
temp = input_n
if( input_n != 2 and input_n != 3):
    if(isEven(input_n) == 0):
        temp = temp - 1
        while(temp > 0):
            print(temp, end = " ")
            temp -= 2
        while(input_n > 0):
            print(input_n, end = " ")
            input_n -= 2

    if(isEven(input_n) == 1):
        while(input_n > 0):
            print(input_n, end = " ")
            input_n -= 2
        temp = temp - 1
        while(temp > 0):
            print(temp, end = " ")
            temp -= 2
else:
    print("NO SOLUTION")