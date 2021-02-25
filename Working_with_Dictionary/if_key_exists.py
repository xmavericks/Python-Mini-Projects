Dictionaries
To determine whether a key is in a dictionary, you can use in and not in, just as you can for a list.

Example:

def main():
    nums = {
        1: "one",
        2: "two",
        3: "three",
    }
    print(1 in nums)
    print("three" in nums)
    print(4 not in nums)

if __name__ == "__main__":
    main();

============== =Output= =================

True
False
True


Dictionaries

A useful dictionary function is get(). It does the same thing as indexing, but if the key is not found in the dictionary it returns another specified value instead.

Example:

def main():
  pairs = {1: "apple",
    "orange": [2, 3, 4], 
    True: False, 
    12: "True",
  }

  print(pairs.get("orange"))
  print(pairs.get(7, 42))
  print(pairs.get(12345, "not found"))

if __name__ == "__main__":
  main();


Output:

[2, 3, 4]
42
not found
