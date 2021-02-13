Pattern to be printed:

5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1

Solution Code:

rows = int(input())

for num in range(1,rows+1):
  for k in range(rows+1, num, -1):
    print(rows+1-num,end = " ") # Printing the maximum value --> explanation rows = 5, num at this iteration = 1. Max value = 5+1-1 = 5, afterwards as num increases max value will be decreases
  print("")

  
Below is another piece of code using extra variable for more clarification and visualise this clearly

rows = int(input())
item = 0  # Item here is the largest value at each column in each row --->  eg 5 5 5 5 5, first row value for rows input = 5
for num in range(1,rows+1):
  for k in range(rows+1, num, -1):
    item = rows+1-num
    print(item,end = " ")
  print("")
