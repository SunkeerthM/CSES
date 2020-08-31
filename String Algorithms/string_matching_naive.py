s1 = input()
s2 = input()
l1 = len(s1)
l2 = len(s2)

count = 0
for i in range(l1 - l2 +1 ):
    if(s1[i] == s2[0] and s1[i+l2-1] ==s2[l2-1]):
        if(s1[i: i+l2] == s2):
            count += 1

print(count)