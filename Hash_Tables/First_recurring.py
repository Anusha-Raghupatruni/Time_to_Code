
def first_recurring(array):
    d = dict()
    for item in array:
        if item in d:
            return item
        else:
            d[item]=True
    return None
array = [2,5,1,5,2]
#print(first_recurring(array))

def naive_approach(array):
    l = len(array)
    i = 0
    frc = None
    while(i<l):
        j = i+1
        while(j<l):
            if array[i] == array[j]:
                l = j
                frc = array[j]
                continue
            else:
                j += 1
        i += 1
    return frc
print(naive_approach(array))

