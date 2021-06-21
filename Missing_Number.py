class Solution:
    def MissingNumber(self,array,n):
        Original_sum = n*(n+1)//2
        array_sum = sum(array)
        return Original_sum - array_sum
t = int(input())
for _ in range(0,t):
    n = int(input())
    a = list(map(int,input().split()))
    s = Solution().MissingNumber(a,n)
    print(s)
