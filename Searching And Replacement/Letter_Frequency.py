Letter Frequency


You are making a program to analyze text.
Take the text as the first input and a letter as the second input, and output the frequency of that letter in the text as a whole percentage.

Sample Input:
hello
l

Sample Output:
40

The letter l appears 2 times in the text hello, which has 5 letters. So, the frequency would be (2/5)*100 = 40


-------------------------- Program : ----------------------------------------------

# This function is responsible for calculating frequency
def frequency(appearance, size):
    return int((appearance/size)*100)

# This function is counting the occurence of searching element in original string
def countOccurence(searchingChar, originalString):
    count = 0
    for i in originalString:
        if i == searchingChar:
            count = count + 1
    return count

# Asking input of originalString
originalString = input()
# Asking input for searchingChar inside the original string
searchingChar = input()
# occurence Storing in count variable
count = countOccurence(searchingChar, originalString)
# Printing the output
print(frequency(count, len(originalString)))
