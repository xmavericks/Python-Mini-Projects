# This program will tell you the exact logic behind printing all the Armstrong numbers till a range
Which number is exactly said to be an Armstrong number?
---> A number say for example 153 is said to be an Armstrong number only if sum of cube of all the digit is exactly equal to that number
Explanation --:
digits in 153 are : 1, 5 and 3
cube of all the digits : 1*1*1 = 1, 5*5*5 = 125, 3*3*3 = 27
sum of  cubes of all the digits = 1 + 125 + 27 = 153 == original number
---> This kind of numbers are said to be an Armstrong number

Program to print all Armstrong numbers from 1 - 1000( or any specific range)

specific_range = int(input("Enter a number till which you want to print all Armstrong number: "))

def isArmstrong(num):
    sum=0
    a = num
    
    while num > 0:
        digit = num % 10
        sum = sum + pow(digit,3)
        num = num // 10
    if sum == a:
        return True
    else:
        return False

for x in range(1,specific_range):
    if isArmstrong(x):
        print("\n"+str(x))
        
Output are:

Enter a number : 1000

0

1

153

370

371

407

# EOF reached
