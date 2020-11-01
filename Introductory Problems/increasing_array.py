n = int(input())
numList = list(int(n) for n in input().strip().split())[:n]
min_turns = 0

for i in range(0, n-1):
    if(numList[i+1] >= numList[i]):
        continue
    else:
        min_turns += numList[i]-numList[i+1]
        temp = numList[i]
        numList[i+1] = temp
        

print(min_turns) 