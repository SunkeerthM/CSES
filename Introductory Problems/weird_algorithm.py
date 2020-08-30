'''
CSES Problem Set 
Introductory Problems - Weird Algorithm

# Author 		: Sunkeerth M
# Description	: Consider an algorithm that takes as input a positive integer n. 
  				  If n is even, the algorithm divides it by two, and if n is odd, 
  				  the algorithm multiplies it by three and adds one. 
  				  The algorithm repeats this, until n is one. For example, the sequence 
  				  for n=3 is as follows: 3→10→5→16→8→4→2→1
  				  Your task is to simulate the execution of the algorithm for a given value of n.

# Date			: 19-07-2020

'''

def isEven(n) : 
	return (n & 1);

input_n = int(input())
print(input_n, end = " ")
while(input_n != 1):
	if(isEven(input_n) == 0 ):
		input_n = int(input_n/2)
		print(input_n, end = " ")
	else:
		if(input_n ==1):
			break;
		else:
			input_n = (3 * input_n) + 1
			print(input_n, end = " ")

