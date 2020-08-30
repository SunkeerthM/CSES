'''
CSES Problem Set 
Introductory Problems - Repetitions

# Author        : Sunkeerth M
# Description   : You are given all You are given a DNA sequence: a string consisting of 
                  characters A, C, G, and T. Your task is to find the longest repetition in 
                  the sequence. This is a maximum-length substring containing only one type 
                  of character.

# Date          : 19-07-2020

'''

def maxRepeating(str): 
  
    l = len(str) 
    count = 0
    res = str[0]
    cur_count = 1 
    for i in range(l):           
        if (i < l-1 and str[i] == str[i + 1]):
            cur_count += 1
        else:
            if cur_count > count : 
                count = cur_count 
                res = str[i]
            cur_count = 1    
    return count 

DNA_seq = input()
print(maxRepeating(DNA_seq))