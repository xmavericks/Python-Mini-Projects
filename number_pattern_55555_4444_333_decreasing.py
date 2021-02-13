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
