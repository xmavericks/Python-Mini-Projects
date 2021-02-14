Mirror Patter:

1 2 3 4 5 # Consider this first half, code from line 18 - 21 is responsible for printing first half
1 2 3 4 
1 2 3 
1 2 
1 
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

Solution Code:

rows = int(input())

for num in range(1,rows+1):
    for k in range(rows+1, num, -1):
        print(rows-k+2,end = " ")
    print("")
for num in range(1,rows+1):
    for i in range(1,num+1):
        print(i, end = " ")
    print("")
