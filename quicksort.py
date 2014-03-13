#!/usr/bin/python

def quickSort(items, first, last):

	if last > first:

		point = first
		keypoint = last

		while not point == keypoint:

			if ((point > keypoint and items[point] > items[keypoint]) 
				or (keypoint > point and items[keypoint] > items[point])):

				tmpItem = items[point]
				items[point] = items[keypoint]
				items[keypoint] = tmpItem

				tmpPoint = point
				point = keypoint
				keypoint = tmpPoint

			if point > keypoint:
				point -= 1
			elif keypoint > point:
				point += 1

		items = quickSort(items, first, point - 1)
		items = quickSort(items, point + 1, last)

	return items[::-1]