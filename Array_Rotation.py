def naive_rotation(array,k):
    new_array = []
    for i in range(k%len(array)):
        new_array.append(array[len(array)-k+i])
    for i in range(len(array)-k % len(array)):
        new_array.append(array[i])
    return new_array


#print(naive_rotation(array,k))

def reverse(array,start,end):
    while start < end:
        array[start],array[end] = array[end],array[start]
        start += 1
        end -= 1
    return array
array = [1,2,3,4,5,6,7,8,9]
k = 2
def reverse_rotate(array,k):
    array = reverse(array,0,len(array)-1)
    array = reverse(array,0,k%len(array)-1)
    array = reverse(array,k%len(array),len(array)-1)
    return array
print(reverse_rotate(array,k))
    

