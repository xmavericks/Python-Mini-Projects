# This is a program where you will get to learn behind the scene of find and replace with.
Say for example, we have shortcut key ctrl + H in Notepad++ where we can replace any word or character, with new word.

Example - 

phrase - '''Hi my name is Amod Kumar, I came from Software Engineering Background. I always wanted to be a Scientist but end up becoming an Engineer'''
say, we want to replace name Amod with new name - Mahesh and the entire phrase will be changed for Amod Kumar to for Mahesh Kumar.


------------------------Program--------------------------
# First line take the input for the original Phrase
phrase = input("Please input some paragraph as your initial phrase, say for example you can tell me something about yourself? : ")
print("Do you want to modify anything in your phrase? : \n",phrase)
boolean = input("Yes/No : ")  # This boolean will ask if he wants to modify anything

# Conditional Statement added here to ask users if they want to change anything
if boolean = "Yes" or "yes" or "YES":
  OldWord = input("What would like to change in your earlier phrase? : ")
  print("You want to replace this - ", OldWord)
  NewWord = input("Enter replacing word here : ")
  

# This function will look for word user want to change
def replacingWord(OldWord):
  ct = phrase.find(OldWord)
  return ct

# This funtion will allow users to change their previous word with new word orwords
def replaceWith(NewWord):
  ct = phrase.replace(OldWord, NewWord)
  return ct
