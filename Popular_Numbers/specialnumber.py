# special number are number whose sum of factorials of all the digits are equal to the original number.
Example - 145 is a special number
Why?
1! + 4! + 5! = 1 + 24 + 120 == 145 = Original number

--------------------Program---------------------------

number = int(input("Enter a number: "))

def specialnumber(number):
    copy_of_number = number
    sumOfDigits = 0
    # This function will be accountable for finding the sum of factorial of each digit of a number
    while (copy_of_number != 0):
       #Get the rightmost digit 
        currentDigit = copy_of_number % 10
        sumOfDigits = sumOfDigits + factorial(currentDigit)
        copy_of_number = copy_of_number // 10
        
    #If sumOfDigits is equal to inputNumber then the number is Special, otherwise not
    if (sumOfDigits == number):
        return True
    else:
        return False
# Function declared for calculating factorial of digits
def factorial(n):
    if (n == 1 or n == 0):
        return 1
    else:
        return (n * factorial(n -1))
        
result = specialnumber(number)

if (result == True):
    print(str(number) + " is a Special number")
else:
    print(str(number) + " is NOT a Special number")
    
  
--------------------Output---------------------------

Enter a number: 40585
40585 is a Special number
