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
