# This program is added for bubble sort.

# For very large value of length of Array -> It will fail
# Try to check the constraint, if n = lenght of array > 1000, it will give Time Limit Exceeded

Program : 1 -  without using third variable for swapping elements
  
arr = [1, 5, 3, 2]

def bubble_sort(arr):
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
              arr[j] = arr[j] + arr[j+1]
              arr[j+1] = arr[j] - arr[j+1]
              arr[j] = arr[j] - arr[j+1]
    return arr
print(bubble_sort(arr))

Output:
    
1 2 3 5


Program : 2 - using third variable for swapping elements
  
arr = [1, 5, 3, 2]

def bubble_sort(arr):
    for i in range(n-1,0,-1):
        for j in range(i):
            if arr[j] > arr[j+1]:
            temp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = temp
    return arr
print(bubble_sort(arr))

Output:
    
1 2 3 5
