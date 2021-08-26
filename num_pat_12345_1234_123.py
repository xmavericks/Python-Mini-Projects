Number Patter increasing - element removed at each level having maximum value

1 2 3 4 5 
1 2 3 4 
1 2 3 
1 2 
1

Solution Code:

rows = int(input())

for num in range(1,rows+1):
  for k in range(rows+1, num, -1):
    print(rows-k+2,end = " ") # This line is the reason why, number has been started gettin printed from 1
  print("")

  #EOF Reached
  
