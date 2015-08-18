def main():
	strList = acceptInput()
	print altConcat(strList)

def acceptInput():
	arrLen = int(raw_input("Enter the number of elements: "))
	arr = []
	for x in range(0, arrLen):
		arr.append(raw_input("Enter element #" + str(x + 1) + " "))
	return arr

def altConcat(strList):
	i = 0
	j = 1
	resList = []
	count = 0;
	arrLen = len(strList)
	while(((i + 2) < arrLen) and ((j + 2) < arrLen)):
		resList.append([strList[i] + strList[i + 2]])
		resList.append([strList[j] + strList[j + 2]])
		i += 4
		j += 4
	if not (i + 2) < arrLen:
		if i < arrLen:
			resList.append([strList[i]])
		if j < arrLen:
			resList.append([strList[j]])
		return resList
	elif not (j + 2) < arrLen:
		resList.append([strList[i] + strList[i + 2]])
		resList.append([strList[j]])
		return resList

if "__main__":
	main()