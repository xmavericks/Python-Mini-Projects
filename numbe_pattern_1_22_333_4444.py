Pattern:

1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5

Solution Code below:

Program: Using program

rows = int(input())

for num in range(1,rows+1):
    for i in range(1,num+1):
        print(num, end = " ")
    print(" ")
