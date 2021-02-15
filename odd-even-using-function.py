# Print odd / even number upto a limit n with space separated integer using two separate function - A logic for building threads inter comunication channel
ex - 
n = 10
output should be - 1 2 3 4 5 6 7 8 9 10


Soultion Code:
  
n = int(input("Enter limit upto which you want to print numbers: "))
counter = 1

# Function responsible for printing Odd numbers
def Odd(counter):
    if counter % 2 == 1:
        return counter
        counter+= 1 # Incrementing counter at each iteration
    
# Function responsible for printing Even numbers    
def Even(counter):
    if counter % 2 == 1:
        return counter
        counter += 1 # Incrementing counter at each iteration

for i in range(1, n+1): # Initial iteration range(1,n+10)
    if i == counter:
        Odd(i)
        print(i, end=" ") # Space separated Odd numbers
    else:
        Even(i)
        print(i, end = " ") # Space separated Even numbers

        
Output:
Enter limit upto which you want to print numbers: 20
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20



Some of you might think, that this can be achieved only using 4 lines of code. I agree, but please read the very first line again and then saw 4 liner below:
 
n = int(input("Enter limit to which you want to print numbers: "))

# EOD reached
