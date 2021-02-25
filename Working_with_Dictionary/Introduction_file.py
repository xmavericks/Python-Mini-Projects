Dictionaries

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
