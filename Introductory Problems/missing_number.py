'''
CSES Problem Set 
Introductory Problems - Missing Number

# Author 		: Sunkeerth M
# Description	: You are given all numbers between 1,2,…,n except one. Your task is to 
			      find the missing number. Input - The first input line contains an
			      integer n. The second line contains n−1 numbers. Each number is distinct
			      and between 1 and n (inclusive).Output - Print the missing number.

# Date			: 19-07-2020

'''
import math
sum_limit = int(input())
inp_list = list(map(int,input().split()))

list_sum = int((sum_limit * (sum_limit + 1)) / 2) - sum(inp_list)
print(list_sum)