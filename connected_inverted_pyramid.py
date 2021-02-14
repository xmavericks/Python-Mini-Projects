Pattern - Connected Inverted pyramind pattern 1

5 4 3 2 1 1 2 3 4 5
5 4 3 2 2 3 4 5
5 4 3 3 4 5
5 4 4 5
5 5

Solution Code:

rows = int(input())

for num in range(1,rows+1):
	for k in range(rows+1, num, -1):
        print(k-1,end = " ")			# This line is changed in the next pattern below
    for i in range(num,rows+1):
        print(i, end = " ")				# This line is also changed
    print("")
	

Pattern - Connected Inverted Pyramid pattern - 2

1 2 3 4 5 5 4 3 2 1 
1 2 3 4 4 3 2 1 
1 2 3 3 2 1 
1 2 2 1 
1 1

Code Solution:

rows = int(input())

for num in range(1,rows+1):
    for k in range(rows+1, num, -1):
        print(rows+2-k,end = " ")
    for i in range(num,rows+1):
        print(rows+1-i, end = " ")
    print("")


#EOF reached
