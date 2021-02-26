# Tuple Unpaccking

Tuple Unpacking ~
Tuple unpacking allows you to assign each item in a collection to a variable.

Example:

numbers = (1, 2, 3, 4)
a,b,c,d = numbers
print("a is : ",a, "\nb is : ",b, "\nc is : ", c, "\nd is : ", d)

Output:

a is :  1 
b is :  2 
c is :  3 
d is :  4


Tuple Unpacking
A variable that is prefaced with an asterisk (*) takes all values from the collection that are left over from the other variables.

Example : 

a, b, *c, d = (1, 2, 3, 4, 5, 6, 7, 8, 9) or [1, 2, 3, 4, 5, 6, 7, 8, 9]  -- we can initiate using either square bracket or parenthesis
print(a)
print(b)
print(c)
print(d)

___ Output ___
a is :  1
b is :  2
*c Holds all values till last item :  [3, 4, 5, 6, 7, 8]
d is :  9
