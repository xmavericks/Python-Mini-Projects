Dictionaries:
We saw how lists allow to store elements with their corresponding indices.
The indices in a list are automatically set. But what if we need to set our own index?

Dictionaries are another collection type and allow us to map arbitrary keys to values.
Dictionaries can be indexed in the same way as lists, using square brackets containing keys.

Example:-

def main():
    ages = {
        "Maya": 27, 
        "Mahi": 26, 
        "Ashu": 25
    }
    print("Ashu's age is : ",ages["Ashu"])
    print("Mahi's age is : ",ages["Mahi"])
    
if __name__ == "__main__":
    main();

-------Output:::::::::::
Ashu's age is : 25
Mahi's age is : 26

Important NOTE : Each element in a dictionary is represented by a key:value pair.

Key Value should comparise:
You can use strings, integers, booleans, and any other immutable type as dictionary keys.
This means that you cannot use lists or dictionaries as keys:

------------------------------------Example code:
bad_dict = {
    [1, 2, 3]: "one two three", 
}

------------------------------------Output Error:
Traceback (most recent call last):
File "file0.py", line 1, in <module>
bad_dict = {
TypeError: unhashable type: 'list'

:::::::::::::::::::Example 2:------------------------------------

def main():
    try:
        bad_dict = {
            [1, 2, 3]: "one two three", 
        }
    except:
        print("Key value should comparise list as keys")
        print("Type Error: unhashable type: \'list'")

if __name__ == "__main__":
    main();

::::::::::::::::::: Output ::::::::::::::
Key value should comparise list as keys
Type Error: unhashable type: 'list'
