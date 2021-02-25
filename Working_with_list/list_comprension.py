# This file contains a basic example to print all the numbers from 0-100 which is multiple of both 3 and 5 using list comprehension


------------------ Program: Python -----------------------------

def main():
    upperLimit = int(input("Enter Upper limit: "))
    def multipleof_3_and_5(upperLimit):
        res = [x for x in range(100) if x%3== 0 if x%5==0]
        
        for i in res:
            print(i, end=" ")
    
    multipleof_3_and_5(upperLimit)

if __name__ == "__main__":
    main();

--------------------Output: -----------------------------------
