s1 = input()
l1 = len(s1)

for i in range(1, l1-1):
	t1 = s1[0:i]
	t2 = s1[l1 -i: l1]
	if(t1 == t2):
		print(len(t1), "", end = "")