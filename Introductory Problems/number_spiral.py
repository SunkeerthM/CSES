'''
CSES Problem Set 
Introductory Problems - Number Spiral

# Author        : Sunkeerth M
# Description   : https://cses.fi/problemset/task/1071

# Date          : 20-07-2020

'''
def num_spi(a,b):
    M = max(a, b)
    return (a - b) * (-1) ** M+M * M - M + 1

fin_array = list()
test_case = int(input())
for i in range(test_case):
    inp = list(map(int, input().split()))
    a = inp[0]
    b = inp[1]
    fin_array.append(num_spi(a, b))

for j in fin_array:
    print(j)