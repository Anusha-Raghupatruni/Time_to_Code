def naive_move_zeroes(array):
    l = len(array)
    for i in range(l):
        if array[i]==0:
            array.append(0)
    j = 0
    c = 0
    while c<l:
        if array[j] != 0:
            j+=1
        else:
            array.pop(j)
        c+=1
    return array
array = [0,0,0,0,1,0,3,0,0,12,9,7]
#print(naive_move_zeroes(array))

def swap_move(array):
    z = 0
    for i in range(len(array)):
        if array[i] != 0:
            array[i],array[z] = array[z],array[i]
            z += 1
        print(array[i],array[z])
    return array
#print(swap_move(array))

def one_linear_move(array):
    array.sort(key=bool,reverse=True)
    return array
print(one_linear_move(array))
