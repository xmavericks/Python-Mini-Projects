def main():
	arr = [2, 1, 4, 5, 3, 8, 7, 6, 10, 9, 11]
	arr.sort()
	n = len(arr)-1
	low, high = 0, n
	print(arr)
 
	def search(arr, low, high, x):
		if low <= high:
			mid = low + (high-low) // 2
			if arr[mid] < x:
				low = mid + 1
				return search(arr, low, high, x)
			elif arr[mid] > x:
				high = mid - 1
				return search(arr, low, high, x)
			else:
				print("Element is found at: ", mid)
		else:
			print("Element is not present in the given array: ", arr)
	search(arr,low, high,8)

if __name__ == "__main__":
	main();

Output :
searching element = 8
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
Element is found at:  7
