# Reversing two number using tuple unpacking and also find sum of the number

numbers = (1, 2)
a,b = numbers
print("a is : ",a, "\nb is : ",b)
a, b, sum = b, a, a+b
print("a is now : ",a, "\nb is now : ",b, "\nSum of a and b is : ", sum)

___ Output ____

a is :  1 
b is :  2
a is now :  2 
b is now :  1 
Sum of a and b is :  3
