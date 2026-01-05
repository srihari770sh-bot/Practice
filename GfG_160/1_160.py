class Solution:
    def getSecondLargest(self, arr):
        n=len(arr)
        if n < 2:
            return -1
        fst=scd=float('-inf')
        for num in arr:
            if num > fst:
                scd=fst
                fst=num
            elif num>scd and num<fst:
                scd=num
        if scd==float('-inf'):
            return -1
        else:
            return scd
a = [12,34,10,35]
sol = Solution()
print(sol.getSecondLargest(a))