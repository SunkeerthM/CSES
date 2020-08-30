  
'''
CSES Problem Set 
Sorting and Searching - Distinct Numbers
# Author 		: Sunkeerth M
# Description	: You are given a list of n integers, and your task is to calculate the number of 
				  distinct values in the list. 
				  The first input line has an integer n: the number 
				  of values. The second line has n integers x1,x2,…,xn. 

				  Output:Print one integers: the number of distinct values.

# Date			: 10-08-2020
--------------------------------------------------------------------------------------------------
n = int(input())
duplicate_ar = list(map(int,input().split())) 
unique_no = len(set(duplicate_ar))
print(unique_no )
'''
n = input()
print(len(set(list(map(int,input().split())))) )


