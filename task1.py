def main():
	arr = acceptInput()
	print arr
	print arrSort(arr)
	# print arrSort(['ccc','bbb','a', '#', 'aaa'])
	print arrSort([])

def checkArr(arr):
	for x in range(0, len(arr)):
		if not arr[x].isalpha():
			return False
	return True

def arrSort(arr):
	if checkArr(arr):
		if len(arr) == 0:
			return "Empty Array"
		else:
			arr.sort()
			return arr
	else:
		return "Not array of Names"

def acceptInput():
	arrLen = int(raw_input("Enter the number of elements: "))
	arr = []
	for x in range(0, arrLen):
		# arr = arr + [raw_input("Enter element #" + str(x + 1) + " ")]
		arr.append(raw_input("Enter element #" + str(x + 1) + " "))
	return arr

if "__main__":
	main()