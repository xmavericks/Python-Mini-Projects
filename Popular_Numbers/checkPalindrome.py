# Any number is said to be a Palindrome, if and only if all the digits are same from both ends
Example - 121 == 121, 123 != 321
---------------------------Program 1 : Taking input as a String-------------------------------

number = int(input("Enter number to check if it is a palindrome or not: "))
copy_of_number = number
def checkPalindrome(number):
    reverse = 0
    while(number>0):
        digit = number % 10
        reverse = (reverse * 10) + digit
        number = number // 10
    if(copy_of_number == reverse):
        print("Palindrome")
    else:
        print("Not a palindrome!")
checkPalindrome(number)

--------------------------Program 2 : Taking input as a String-------------------------------
    
n, result, comparator = input("Enter number to check if it is a palindrome or not: "),[], []
result.append(n[::-1])
comparator.append(n[0:])
def checkPalindrome(n):
    flag = False
    if result == comparator:
        flag = True
    if flag == True:
        print("Palindrome")
    else:
        print("Not a Palindrome")
checkPalindrome(n)

----------------------Output----------------------
Enter number to check if it is a palindrome or not: 12345678987654321
Palindrome
