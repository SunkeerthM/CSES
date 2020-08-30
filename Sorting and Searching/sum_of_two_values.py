'''
CSES Problem Set 
Sorting and Searching - Sum of Two Values
# Author        : Sunkeerth M
# Description   : https://cses.fi/problemset/task/1640
# Date          : 10-08-2020
'''
   
n, ar_sum = map(int,input().split())
arr =  list(map(int,input().split()))
d_1 = dict()

for i in range(n):
    p = arr[i]
    if ar_sum - p in d_1:
        print(i+1, d_1[ar_sum-p] + 1)
        quit()


    else:
        d_1[p] =  i

print("IMPOSSIBLE")













