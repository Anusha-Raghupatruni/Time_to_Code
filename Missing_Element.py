def missing_num(array,n):
    original_sum = n*(n+1)//2
    array_sum = sum(array)
    return original_sum - array_sum
array = [1,2,3,4,5,6,8,9]
n = 9
print(missing_num(array,9))
