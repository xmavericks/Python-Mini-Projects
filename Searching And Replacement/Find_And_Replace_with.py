# This is a program where you will get to learn behind the scene of find and replace with.
Say for example, we have shortcut key ctrl + H in Notepad++ where we can replace any word or character, with new word.

Example - 

phrase - '''Hi my name is Amod Kumar, I came from Software Engineering Background. I always wanted to be a Scientist but end up becoming an Engineer'''
say, we want to replace name Amod with new name - Mahesh and the entire phrase will be changed for Amod Kumar to for Mahesh Kumar.


------------------------Program--------------------------
# First line take the input for the original Phrase
phrase = input("Please input some paragraph as your initial phrase, say for example you can tell me something about yourself? : ")
print("Is this phrase correct according to you? : \n",phrase)

# This boolean will ask if he wants to modify anything
boolean = input("Yes/No : ")


# This function will look for word user want to change
def replacingWord(change):
  ct = phrase.find(change)
  return ct

# This funtion will allow users to change their previous word with new word orwords
