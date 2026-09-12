class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maxi = -1
        out = [-1 for _ in range(len(arr))]

        for i in range(len(arr)-1, -1, -1):
            out[i] = maxi
            if arr[i] > maxi:
                maxi = arr[i]
        
        return out