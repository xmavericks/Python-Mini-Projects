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
    item = rows+1-num  # As explained in line number 15 above, this is the same value of item which you can see gets printed after each iteration for for loop on line 14 and output line 15
    print(item,end = " ")
  print("")

  
Output for this code will be same as the above:
    
5 5 5 5 5 
4 4 4 4 
3 3 3 
2 2 
1


Below is the output will expain even better what I meant to say, count number of stars at on each column and match with the number from above pattern. now you can say,
the max value, which I was talking about the exact highest value, which is represented here by star to provide better visualization

***** ***** ***** ***** ***** ----> 5 5 5 5 5
**** **** **** ****           ----> 4 4 4 4
*** *** ***                   ----> 3 3 3
** **                         ----> 2 2
*                             ----> 1

# End of file reached, thanks for visiting
