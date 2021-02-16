rows = int(input())

print("\nPattern 1: \n")
#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

for num in range(1,rows+1):
  for k in range(rows, num, -1): # created for loop to print extra spaces
    print(" ",end = " ")
  for i in range(1, num+1):  # This loop is responsible for printing values right? But we have to print spaces before the value, see line number 3 - there are 4 spaces printed before 1
    print("*", end = " ")
  print("")

print("\nPattern 2: \n") 
#   * 
#   * * 
#   * * * 
#   * * * * 
#   * * * * *

for num in range(1,rows+1):
  for k in range(rows, num, -1): # created for loop to print extra spaces
    print("",end = "")
  for i in range(1, num+1):  # This loop is responsible for printing values right? But we have to print spaces before the value, see line number 3 - there are 4 spaces printed before 1
    print("*", end = " ")
  print("")

print("\nPattern 3: \n")
#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * *
for num in range(1,rows+1):
  for k in range(rows, num, -1): # created for loop to print extra spaces
    print("",end = " ")
  for i in range(1, num+1):  # This loop is responsible for printing values right? But we have to print spaces before the value, see line number 3 - there are 4 spaces printed before 1
    print("*", end = " ")
  print("")

print("\n Pattern 4: \n")
#   ********* 
#   ******* * 
#   ***** * * 
#   *** * * * 
#   * * * * *
for num in range(1,rows+1):
  for k in range(rows, num, -1): # created for loop to print extra spaces
    print("*",end = "*")
  for i in range(1, num+1):  # This loop is responsible for printing values right? But we have to print spaces before the value, see line number 3 - there are 4 spaces printed before 1
    print("*", end = " ")
  print("")
  
print("\n Pattern 5: \n")
#   * * * * * 
#   * * * * 
#   * * * 
#   * * 
#   *
for num in range(1,rows+1):
  for k in range(rows+1, num, -1):
    print("*",end = " ") # Printing the maximum value --> explanation rows = 5, num at this iteration = 1. Max value = 5+1-1 = 5, afterwards as num increases max value will be decreases
  print("")
