Printing Pattern :
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5

Note - I am showing you two ways to print the above pattern, please note it can have more than 2 solutions to print the above pattern

Program: 1

rows = int(input())

for num in range(1,rows+1):
  for i in range(1,num+1): # here why I iterate through 1 - (num+1) --> this simply means for(i = 1; i <= num; i++) like we use in C++/JavaScript
    print(i, end = " ")
  print("")
  
Program: 2
  
rows = int(input())

for num in range(1,rows+1):
  for i in range(1,num):    # This line is not iterating like earlier, Think???
    print(i, end = " ")
  print(num)                # This line is changed, think why and how?
