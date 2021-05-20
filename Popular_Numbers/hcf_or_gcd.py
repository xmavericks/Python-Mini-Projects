# This file contains the method to calculate GCD/HCF of two numbers

Method 1: Using recursive approach 1
#using the library function
from fractions import gcd
def main():
  a , b = int(input()), int(input())
	def gcd(a,b):
	    if a == 0:
	    	return b
	    return gcd(b % a, a)
	print(gcd(a,b))

if __name__ == "__main__":
	main();

  
Method 2: Using recursive approach 2
# Recursive function to return gcd of a and b
def gcd(a,b):
     
    # Everything divides 0
    if (a == 0):
        return b
    if (b == 0):
        return a
 
    # base case
    if (a == b):
        return a
 
    # a is greater
    if (a > b):
        return gcd(a-b, b)
    return gcd(a, b-a)

a = int(input())
b = int(input())
if(gcd(a, b)):
    print('GCD of', a, 'and', b, 'is', gcd(a, b))
else:
    print('not found')
