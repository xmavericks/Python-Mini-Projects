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

