Pattern problem:

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5


Program code solution in Python:
  
rows = int(input())

for num in range(1,rows+1):
  for k in range(rows+1, num, -1): # Dereasing for loop used to decrease the number of elements inside each decreasing row afterwards
    print(num,end = " ") # Printing number, since we want it in increasing order, and num initially inside this loop has value 1, and then num ++ applied at each iteration
  print("")
