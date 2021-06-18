Don't get confused, from the previous pattern

Previous Pattern was :
        1
      1 2  -> Line has increasing value
    1 2 3 
  1 2 3 4 
1 2 3 4 5
Current Pattern:
        1 
      2 2 -> Line has same value, but increased by 1 from previous line, simply means print the number times number of rows - rows 2 , line 2 should be 22 with (rows-2) spaces after
    3 3 3 -> space_count = rows-3, beacuse this is 3rd row, so we substracted 3
  4 4 4 4 
5 5 5 5 5

Now, Since we have already completed writing the program for previous pattern, I will still compare both the programs which will give you what is happening in both codes. Also
I will try to show you using -> replacement of spaces with * for clear understanding

Previous pattern                                                        Present Patter
        1                                                                       1
      1 2                                                                     2 2
    1 2 3                                                                   3 3 3
  1 2 3 4                                                                 4 4 4 4
1 2 3 4 5                                                               5 5 5 5 5

Code -                                                                  Code -

rows = int(input())                                                     rows = int(input())

for num in range(1,rows+1):                                             for num in range(1, rows+1):
  for k in range(rows, num, -1):                                          for k in range(rows, num, -1):
    print("*",end = " ")                                                    print("*",end=" ")
  for i in range(1, num+1):                                               for i in range(1, num+1):
    print(i, end = " ")               <---- Difference ---->                print(num, end = " ")
  print("")                                                               print("")
        

Note : number of rows taken as input was - 5

Output Program 1 - Left hand side -----> Printed star (*) in place of spaces for clear visualisation
* * * * 1
* * * 1 2
* * 1 2 3
* 1 2 3 4
1 2 3 4 5

Output Program 2 - Right hand side -----> Printed star (*) in place of spaces for clear visualisation
* * * * 1
* * * 2 2
* * 3 3 3
* 4 4 4 4
5 5 5 5 5

# End of this file has reached
