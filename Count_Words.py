words = input("Enter any sentence want : ")
count = 1
for w in words:
  if w == " ":
    count += 1
print("Total number of words entered by you are: "+str(count))

Output - 
Enter any sentence want: leetcode is awesome # Entered this sentence
Total number of words entered by you are: 3
