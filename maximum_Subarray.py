def brute_force_max_subarray(array):
    maximum = 0
    if len(array) == 0:
        return None
    for i in range(len(array)):
        cum_sum = 0
        for j in range(i,len(array)):
            cum_sum += array[j]
            maximum = max(maximum,cum_sum)
    return maximum
array = [-2,1,-3,4,-1,2,1,-5,4]
#print(brute_force_max_subarray(array))

def kadane_algo(array):
    maximum = maxarray = array[0]
    for i in range(1,len(array)):
        maxarray = max(array[i],maxarray+array[i])
        maximum = max(maxarray,maximum)
        print(maximum,maxarray)
    return maximum
print(kadane_algo(array))
