Pattern reversed:

        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5

Solution Code:

Program - Using Python

rows = int(input())

for num in range(1,rows+1):
  for k in range(rows, num, -1): # created for loop to print extra spaces
    print(" ",end = " ")
  for i in range(1, num+1):  # This loop is responsible for printing values right? But we have to print spaces before the value, see line number 3 - there are 4 spaces printed before 1
    print(i, end = " ")
  print("")
  
 Note - The above program can has below cleared explanation, for watching exact number of spaces getting print before actual values
        Let's try to print * in place of space as in line number 17 for iteration of k
 
Program  - se, and try to understand

rows = int(input())

for num in range(1,rows+1):
    for k in range(rows,num,-1):
        print("*",end = " ") # Line number 17 from above is changed and instead of printing space, we are print *. See output pattern generated for clear understanding
    for i in range(1,num+1):
        print(i,end=" ")
    print("")

Output:

* * * * 1  - There were 4 spaces getting printed from above first program
* * * 1 2 
* * 1 2 3 
* 1 2 3 4 
1 2 3 4 5 - In this line since, this rows occupied maximum values of entries, no spaces / * getting printed
