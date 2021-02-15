Print first and last name in reverse order with a space between them - >

example - 
first_name = amod
last_name = kumar

output should be = kumar amod

Code solution: Solution 1 using 4 for loops for every basic iteration and reversing only name -> example amod kumar --> kumar amod
  
first_name = input("Enter your first name: ") # Taking input of first name
last_name = input("Enter your last name: ")   # Taking input of last name
f_name_reverse = []                           # Declaring list variable to store reversed names respectively
l_name_reverse = []
first_name_reversed = ""                      # Declaration of empty string variable fo storing each char from reversed name and append it invertly
last_name_reversed = ""
for i in range(len(first_name)):
    f_name_reverse.append(first_name[i])      # Performing reversing of letter
for j in range(len(last_name)):
    l_name_reverse.append(last_name[j])

for k in range(len(f_name_reverse)):          # storing in empty string
    first_name_reversed += f_name_reverse[k]
for l in range(len(l_name_reverse)):
    last_name_reversed += l_name_reverse[l]
print("First name was: ",first_name)
print("Last name was: ",last_name)
print("Reversed name is: "+last_name_reversed+" "+first_name_reversed)


Output expected as above and after running the above code is:
Enter your first name: amod
Enter your last name: kumar
First name was:  amod
Last name was:  kumar
Reversed name is: kumar amod
  
  
Solution 2 using 2 for loops for every basic iteration and reversing each character of each name --> example amod kumar --> ramuk doma

# Expected output:
# first_name = amod
# last_name = kumar

# Output --> ramuk doma

Code:

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
first_name_reversed = ""
last_name_reversed = ""


for i in range(len(first_name)-1,-1,-1):
    first_name_reversed += first_name[i]
for j in range(len(last_name)-1,-1,-1):
    last_name_reversed += last_name[j]
    

print("First name was: ",first_name)

print("Last name was: ",last_name)

print("Reversed name is: "+last_name_reversed+" "+first_name_reversed)

#Expected output matches exact output:

Enter your first name: amod
Enter your last name: kumar
First name was:  amod
Last name was:  kumar
Reversed name is: ramuk doma
