Average Word Length


Given a sentence as input, calculate and output the average word length of that sentence.
To calculate the average word length, you need to divide the sum of all word lengths by the number of words in the sentence.

Sample Input:
this is some text

Sample Output:
3.5

Explanation: There are 4 words in the given input, with a total of 14 letters, so the average length will be: 14/4 = 3.5

    
--------------------Program : Python -------------------------------------
  
def main():
    text = input()
    def countWords(text):
        count = len(text.split())
        return count

    def sumOfLengthofWord(text):
        sum = 0
        l = text.split()
        string = [x for x in l]
        
        for i in string:
            sum = sum + len(i)
        
        return sum

    print(sumOfLengthofWord(text)/countWords(text))

if __name__ == "__main__":
    main();
    
    
-------------------------Output: -----------------------------
Test Case I:

coding is awesome
Your Output
5.0
Expected Output
5.0

Test Case II:

Input
I am learning data structures on SoloLearn and its great
Your Output
4.7
Expected Output
4.7
