def main():
	strList = acceptInput()
	print mySort(strList)

def acceptInput():
	arrLen = int(raw_input("Enter the number of elements: "))
	arr = []
	for x in range(0, arrLen):
		arr.append(raw_input("Enter element #" + str(x + 1) + " "))
	return arr

def RepresentsInt(s):
    try:
    	int(s)
    	return True
    except ValueError:
    	return False

def mySort(arr):
	if all(RepresentsInt(x) for x in arr):
		print "Sorting Intergers...."
		arr.sort()
		return arr
	elif all(x.isalpha() for x in arr) and all(isinstance(x, str) for x in arr):
		print "Sorting Strings...."
		arr.sort()
		return arr
	else:
		print "List of Mixed or unkown type"
		arr.sort()
		return arr

if "__main__":
	main()