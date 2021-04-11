--------------------Program-----------------------
n, result, comparator= input("Enter number to check if it is a palindrome or not: "),[], []
result.append(n[::-1])
comparator.append(n[0:])
def checkPalindrome(n):
    flag = False
    if result == comparator:
        flag = True
    if flag == True:
        print(n," : is a Palindrome")
    else:
        print(n,": is not a Palindrome")
checkPalindrome(n)

--------------------Output------------------------

1_________________________________________________________________________
Enter number to check if it is a palindrome or not: amodkumar
amodkumar : is not a Palindrome

2_________________________________________________________________________ 
Enter number to check if it is a palindrome or not: 12345678987654321
12345678987654321 : is a Palindrome

3_________________________________________________________________________
Enter number to check if it is a palindrome or not: 12456987
12456987 : is not a Palindrome

4_________________________________________________________________________
Enter number to check if it is a palindrome or not: 1 2 3 4 redivider 4 3 2 1
1 2 3 4 redivider 4 3 2 1 : is a Palindrome

5_________________________________________________________________________
Enter number to check if it is a palindrome or not: racecar
racecar is a Palindrome
