def binarySearch (array, left, right, search_value):

	if right >= left:

		mid = left + (right - left) // 2

		if array[mid] == search_value:
			return mid
		
		elif array[mid] > search_value:
			return binarySearch(array, left, mid-1, search_value)

		else:
			return binarySearch(array, mid + 1, right, search_value)

	else:
		return -1


array = [ 2, 3, 4, 10, 40 ]
search_value = 10

result = binarySearch(array, 0, len(array)-1, search_value)

if result != -1:
	print ("Element is found at index % d" % result)
else:
	print ("Element is not found")
