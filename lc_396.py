class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        basic_sum = 0
        F0 = 0

        for i in range(0, len(nums)):
            F0 += i * nums[i]
            basic_sum += nums[i]
        max_val = F0
        for i in range(1, len(nums)):
            F0 = F0 + basic_sum - len(nums) * nums[-i]
            max_val = max(max_val, F0)

        return max_val