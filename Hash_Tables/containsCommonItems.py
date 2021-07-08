def containsCommonItem(arr1,arr2):
    for i in range(len(arr1)):
            for j in range(len(arr2)):
                if (arr1[i] == arr2[j]):
                    return True
    return False

arr1 = ['a','b','c','d']
arr2 = ['z','y','a']
#print(containsCommonItem(arr1,arr2))

def commonItem_Hashing(arr1,arr2):
    d = {}
    for i in range(len(arr1)):
        if arr1[i] not in d:
            d[arr1[i]] = True
    for j in range(len(arr2)):
        if arr2[j] in d:
            return True
    return False
print(commonItem_Hashing(arr1,arr2))
