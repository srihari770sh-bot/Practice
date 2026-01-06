class Solution:
    def pushZerosToEnd(self,arr):
        a = 0
        for i in range(len(arr)):
            if arr[i] !=0:
                arr[i],arr[a] = arr[a],arr[i]
                a += 1
        return arr