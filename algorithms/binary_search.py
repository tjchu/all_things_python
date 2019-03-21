# A way to find an element in a sorted list by sarching the middle index then divide and search again in the middle
# O(log(n))

# Python Program for recursive binary search. 

# Returns index of x in arr if present, else -1 
def binarySearch(arr, l, r, x): 
	if r >= l:
		mid = (r+l)//2
		#print("%d + %d divided by 2 is %s (the midpoint)" % (l, r, mid))
		if arr[mid] == x:
			return mid
		if x > arr[mid]:
			return binarySearch(arr, mid+1, r, x)
		elif x < arr[mid]:
			return binarySearch(arr, l, mid-1, x)
	else:
		return -1




# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binarySearch(arr, 0, len(arr)-1, x) 
print(result)