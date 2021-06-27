def merge(array1,array2):
    MergedArray = []
    flag = 0
    first_array_index = second_array_index = 0
    while not (first_array_index >= len(array1) or second_array_index >=
            len(array2)):
        print(array1[first_array_index],array2[second_array_index])
        if array1[first_array_index] <= array2[second_array_index]:
            MergedArray.append(array1[first_array_index])
            first_array_index += 1
        else:
            MergedArray.append(array2[second_array_index])
            second_array_index += 1
        if first_array_index == len(array1):
            flag = 1
    if flag == 1:
        for item in array2[second_array_index:]:
            MergedArray.append(item)
    else:
        for item in array1[first_array_index:]:
            MergedArray.append(item)
    return MergedArray

array1 = [1,3,5,7]
array2 = [2,4,6,8,10,12]
print(merge(array1,array2))

