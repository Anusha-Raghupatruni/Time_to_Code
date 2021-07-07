"""For an integer N find the number of trailing zeroes in N!."""


class Solution:
    def trailingZeroes(self, N):
        if(N < 0):
            return -1
        count = 0
        while(N >= 5):
            N //= 5
            count += N 
        return count




t = int(input())
for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.trailingZeroes(N)
        print(ans)

