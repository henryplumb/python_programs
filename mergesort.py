from quicksort import quickSort

def mergeSort(in1, in2):

	out = []
	point1 = 0
	point2 = 0

	while point1 < len(in1) and point2 < len(in2):

		item1 = in1[point1]
		item2 = in2[point2]

		if item1 < item2:
			out.append(item1)
			point1 += 1
		elif item2 < item1:
			out.append(item2)
			point2 += 1
		else:
			out.append(item1)
			point1 += 1
			point2 += 2

	if point1 > len(in1):
		out += in1[-(len(in1) - point1):]
	elif point2 > len(in2):
		out += in2[-(len(in2) - point2):]

	return out

in1 = input("First data list: ").split(",")
in2 = input("Second data list: ").split(",")

in1 = quickSort(in1, 0, len(in1) - 1)
in2 = quickSort(in2, 0, len(in2) - 1)

print(mergeSort(in1, in2))