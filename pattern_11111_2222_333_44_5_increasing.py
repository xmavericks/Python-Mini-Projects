Pattern problem:

1 1 1 1 1 
2 2 2 2 
3 3 3 
4 4 
5


Program code solution in Python:
  
rows = int(input())

for num in range(1,rows+1):
  for k in range(rows+1, num, -1):
    print(num,end = " ")
  print("")
