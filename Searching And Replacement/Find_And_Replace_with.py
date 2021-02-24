# This is a program where you will get to learn behind the scene of find and replace with.
Say for example, we have shortcut key ctrl + H in Notepad++ where we can replace any word or character, with new word.

Example - 

phrase - '''Hi my name is Amod Kumar, I came from Software Engineering Background. I always wanted to be a Scientist but end up becoming an Engineer'''
say, we want to replace name Amod with new name - Mahesh and the entire phrase will be changed for Amod Kumar to for Mahesh Kumar.


------------------------Program--------------------------
# This function will look exact position of the first occurence of replacing word in phrase
# def replacingWord(OldWord):
#   ct = phrase.find(OldWord)
#   return ct

# This funtion will allow users to change their previous word with new word orwords
def replaceWith(OldWord,NewWord):
  ct = phrase.replace(OldWord, NewWord)
  return ct
  
# Asking user for any modifications
def prompt(boolean):
  if boolean == "YES" or boolean == "Yes" or boolean == "yes":
    OldWord = input("What would like to change in your earlier phrase? : ")
    NewWord = input("Enter replacing word here : ")
    print("Your new phrase is : \n" ,replaceWith(OldWord, NewWord))    
  else:
    print("Your phrase is looking good : \n", phrase)
# This line take the input for the original Phrase
phrase = input("tell me something about yourself? : ")
print("Do you want to modify anything in your phrase? : \n",phrase)
boolean = input("Yes/No : ")  # This boolean will ask if he wants to modify anything

prompt(boolean)

------------------------Output-------------------
1 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

tell me something about yourself? : hi there, my name is kumar
Do you want to modify anything in your phrase? : 
 hi there, my name is amod kumar
Yes/No : no
Your phrase is looking good : 
 hi there, my name is kumar

2 -_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_-_

tell me something about yourself? : Hi there, my name is kumar patwa
Do you want to modify anything in your phrase? : 
 Hi there, my name is kumar patwa
Yes/No : YES
What would like to change in your earlier phrase? : my name is
You want to replace this -  my name is
Enter replacing word here : I'm
Your new phrase is : 
 Hi there, my name is Ram Kumar patwa
