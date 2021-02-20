--------------------Program-----------------------
n, result, comparator= input("Enter number to check if it is a palindrome or not: "),[], []
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
--------------------Output------------------------
