def two_sum(array,target):
    if len(array) <= 1:
        return False
    aux_dict = {}
    for i in range(len(array)):
        if array[i] in aux_dict:
            return [aux_dict[array[i]],i]
        else:
            aux_dict[target - array[i]] = i
def two_sum_new(arr,target):
     d = {}
     for i in range(len(arr)):
        if arr[i] not in d:
            if target - arr[i] not in d:
                d[arr[i]] = i + 1
            else:
                return [d[target - arr[i]] , i + 1]
        else:
            if target - arr[i] in d:
                return [d[target - arr[i]] , i + 1]

def twoSum(array,target):
    dict1 = {}
    for i,num in enumerate(array):
        match = target - num
        if num in dict1:
            return [dict1[num],i]
        else:
            dict1[match] = i
array = [2,7,4,12,9]
target = 13
print(twoSum(array,target))

