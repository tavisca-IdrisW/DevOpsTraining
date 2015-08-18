def main():
	arr1 = acceptInput()
	arr2 = acceptInput()
	print printSame(arr1, arr2)

def printSame(arr1, arr2):
	arr3 = []
	for x in range(0, len(arr1)):
		for y in range(0, len(arr2)):
			if arr1[x] == arr2[y]:
				arr3.append(arr1[x])
				break
	return arr3

def acceptInput():
	arrLen = int(raw_input("Enter the number of elements: "))
	arr = []
	for x in range(0, arrLen):
		arr.append(int(raw_input("Enter element #" + str(x + 1) + " ")))
	return arr

# print printSame([1,2,4,7],[1,7,9,4,8])

if "__main__":
	main()
