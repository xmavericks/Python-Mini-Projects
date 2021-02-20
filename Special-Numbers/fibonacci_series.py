# What is Fibonacci sequence?
# Def - The Fibonacci sequence is a series of numbers
# where a number is the addition of the last two numbers, starting with 0, and 1. The Fibonacci Sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55…

How can we print this series using Python?

# We need a input number from user asking, how many terms you want to print?
n = int(input("How many numbers you want to print? : "))  # This will ask user for entering total numbers from series he/she wants to prints

# First we need two initialized variable for value 0 and 1
n1, n2 = 0, 1
# We need a counter variable, which will be responsible for printing each number
count = 0
if n <= 0:
   print("Please enter a positive integer: ")
   n = int(input("Enter positive number again : "))
elif n == 1:
   print("Fibonacci sequence upto",n,":")
   print(n1)
else:
   print("Fibonacci sequence upto",n,":")
   while(count < n):
    print(n1, end=" ")
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count +=1
