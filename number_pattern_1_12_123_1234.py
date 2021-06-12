Printing Pattern :
1  
1 2  
1 2 3  
1 2 3 4  
1 2 3 4 5

Note - I am showing you two ways to print the above pattern, please note it can have more than 2 solutions to print the above pattern

Program: 1

rows = int(input()) # It depends on the number of rows you input, I have run the program using input as 5. That is why it has five rows

for num in range(1,rows+1):
  for i in range(1,num+1): # here why I iterate through 1 - (num+1) --> this simply means for(i = 1; i <= num; i++) like we use in C++/JavaScript
    print(i, end = " ")
  print("")
  
Program: 2
  
rows = int(input()) # It depends on the number of rows you input, I have run the program using input as 5. That is why it has five rows

for num in range(1,rows+1):
  for i in range(1,num):    # This line is not iterating like earlier, Think???
    print(i, end = " ")
  print(num)                # This line is changed, think why and how?

  
  
-----------------------Code in single program---------------------------

rows = int(input())

def way1(rows):
	for num in range(1,rows+1):
	  for i in range(1,num+1):
	    print(i, end = " ")
	  print("")

def way2(rows):
	for num in range(1,rows+1):
	  for i in range(1,num):
	    print(i, end = " ")
	  print(num)


print("------------------------------------------------------------------------")
print("--------------Printing same pattern using way1--------------------------")
print("------------------------------------------------------------------------")
way1(rows)
print("------------------------------------------------------------------------")
print("--------------Printing same pattern using way2--------------------------")
print("------------------------------------------------------------------------")
way2(rows)
print("------------------------------------------------------------------------")
print("------------------End of Program ---------------------------------------")
print("------------------------------------------------------------------------")


-------------------- Output --------------------------------------------

------------------------------------------------------------------------
--------------Printing same pattern using way1--------------------------
------------------------------------------------------------------------
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5 
1 2 3 4 5 6 
------------------------------------------------------------------------
--------------Printing same pattern using way2--------------------------
------------------------------------------------------------------------
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
------------------------------------------------------------------------
------------------End of Program ---------------------------------------
------------------------------------------------------------------------
