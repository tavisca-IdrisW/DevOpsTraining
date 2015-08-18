def main():
	studList = acceptInput()
	# arr2 = acceptInput()
	stud = findMax(studList)
	print "Max marks are of student: " + stud.name + "with marks" + str(stud.marks)

def findMax(studList):
	maxMarks = 0;
	maxIndex = -1;
	for x in range(0, len(studList)):
		if maxMarks < studList[x].marks:
			maxMarks = studList[x].marks
			maxIndex = x
	return studList[maxIndex]

def acceptInput():
	arrLen = int(raw_input("Enter the number of elements: "))
	arr = []
	for x in range(0, arrLen):
		stud = Student(raw_input("Enter Name: "), int(raw_input("Enter Marks: ")))
		arr.append(stud)
	return arr

# print printSame([1,2,4,7],[1,7,9,4,8])

class Student(object):
	def __init__(self, name, marks):
		self.name = name
		self.marks = marks

if "__main__":
	main()
