def quickSort(items, first, last):

    if last > first:

        point = first
        keypoint = last

        while not point == keypoint:

            if ((point > keypoint and items[point] > items[keypoint]) 
                or (keypoint > point and items[keypoint] > items[point])):
                
                item = items[point]
                items[point] = items[keypoint]
                items[keypoint] = item

            if point > keypoint:
                point -= 1
            elif keypoint > point:
                point += 1

        items = quickSort(items, first, point - 1)
        items = quickSort(items, point + 1, last)

    return items[::-1]

if __name__ == '__main__':
    in1 = ['dog','frog','sheep','pig','leopard','lion','cheetah','steve']
    print(quickSort(in1, 0, len(in1) - 1))
