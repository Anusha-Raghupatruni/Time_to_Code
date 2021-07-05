def Partition(low,high,array):
    pivot_index = low
    pivot = array[pivot_index]
    while low < high:
        while low < len(array) and array[low] <= pivot:
            low += 1
        while array[high]>pivot:
            high -= 1
        if low < high:
            array[low],array[high] = array[high],array[low]
    array[high],array[pivot_index] = array[pivot_index],array[high]
    return high
def quick_sort(low,high,array):
    if (low < high):
        p = Partition(low,high,array)
        quick_sort(low,p-1,array)
        quick_sort(p+1,high,array)
array = [10,7,8,9,1,5]
quick_sort(0,len(array)-1,array)
print(f'Sorted array:{array}')

