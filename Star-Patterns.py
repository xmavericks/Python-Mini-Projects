rows = int(input())

print("\nPattern 1: \n")

#         * 
#       * * 
#     * * * 
#   * * * * 
# * * * * *

for num in range(1,rows+1):
  for k in range(rows, num, -1):
    print(" ",end = " ")
  for i in range(1, num+1):
    print("*", end = " ")
  print("")

print("\nPattern 2: \n")

#   * 
#   * * 
#   * * * 
#   * * * * 
#   * * * * *

for num in range(1,rows+1):
  for k in range(rows, num, -1):
    print("",end = "")
  for i in range(1, num+1):
    print("*", end = " ")
  print("")

print("\nPattern 3: \n")

#     * 
#    * * 
#   * * * 
#  * * * * 
# * * * * *

for num in range(1,rows+1):
  for k in range(rows, num, -1):
    print("",end = " ")
  for i in range(1, num+1):
    print("*", end = " ")
  print("")

print("\n Pattern 4: \n")

#   ********* 
#   ******* * 
#   ***** * * 
#   *** * * * 
#   * * * * *

for num in range(1,rows+1):
  for k in range(rows, num, -1):
    print("*",end = "*")
  for i in range(1, num+1):
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
    print("*",end = " ")
  print("")

print("\n Pattern 6: \n")

#           * * * * * * 
#         * * * * * * 
#       * * * * * * 
#     * * * * * * 
#   * * * * * *

for num in range(1,rows+1):
    for k in range(rows+1, num, -1):
        print(" ", end=" ")
    for i in range(rows+1):
        print("*",end = " ")
        
    print("")

  
  
  
Output :

Enter number of rows: 5

Pattern 1: 

        * 
      * * 
    * * * 
  * * * * 
* * * * * 

Pattern 2: 

* 
* * 
* * * 
* * * * 
* * * * * 

Pattern 3: 

    * 
   * * 
  * * * 
 * * * * 
* * * * * 

Pattern 4: 

********* 
******* * 
***** * * 
*** * * * 
* * * * * 

Pattern 5: 

* * * * * 
* * * * 
* * * 
* * 
*

Pattern 6:
          * * * * * * 
        * * * * * * 
      * * * * * * 
    * * * * * * 
  * * * * * *

# EOF Reached
