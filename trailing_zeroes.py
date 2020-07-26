'''
CSES Problem Set 
Introductory Problems - Trailing Zeroes

# Author        : Sunkeerth M
# Description   : Your task is to calculate the number of trailing zeros in the factorial n!.
				  For example, 20!=2432902008176640000 and it has 4 trailing zeros. The only 
				  input line has an integer n. Output - Print the number of trailing zeros 
				  in n!.

# Date          : 20-07-2020

'''

import math
z_cnt = 0

def no_of_zeros(n):
    count = 0
    i=5
    while (n/i>=1): 
        count += int(n/i) 
        i *= 5
    return int(count)

temp = (int(input()))
z_cnt = no_of_zeros(temp)
print(z_cnt)