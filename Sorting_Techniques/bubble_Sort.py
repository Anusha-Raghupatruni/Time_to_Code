def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(0,n-i-1):
            if array[j+1]<array[j]:
                array[j],array[j+1] = array[j+1],array[j]

array = [3,1,5,4,6,2,9]

def smart_bubblesort(array):
    n = len(array)
    for i in range(n):
        swapped = False
        for j in range(0,n-i-1):
            if array[j]>array[j+1]:
                array[j],array[j+1] = array[j+1],array[j]
                swapped = True
        if swapped == False:
            break
smart_bubblesort(array)
for i in range(len(array)):
    print("%d"%array[i],end = " ")
