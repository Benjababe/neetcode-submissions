class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lr = [1] * len(nums)
        for i, n in enumerate(nums):
            lr[i] = lr[i-1] * n
        
        rl = [1] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            if i < len(nums)-1:
                rl[i] = rl[i+1] * nums[i]
            else:
                rl[i] = nums[i]

        out = [1] * len(nums)
        for i in range(len(out)):
            if i == 0:
                out[i] = rl[i+1]
            elif i == len(out)-1:
                out[i] = lr[i-1]
            else:
                out[i] = lr[i-1] * rl[i+1]

        return out