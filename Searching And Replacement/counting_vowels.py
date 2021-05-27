Accessing Strings

You need to make a program that counts the number of vowels in a given text.
The vowels are a, e, i, o, and u.
Take a string as input and output the number of vowels.

Sample Input:
this is great

Sample Output:
4

------------------------------Program---------------------------------------
#your code goes here

st = input()
count = 0
for x in st:
    if x == 'a':
        count += 1
    elif x == 'e':
        count += 1
    elif x == 'i':
        count += 1
    elif x == 'o':
        count += 1
    elif x == 'u':
        count += 1
print(count)
