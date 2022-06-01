class Solution:
    def findMin(self, nums: List[int]) -> int:
        # judge if separable
        if nums[-1] >= nums[0]:
            return nums[0]
        # find [k, k+1, ..., n-1][0,...,k-1] index 0 in right
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = l + r >> 1
            if nums[mid] < nums[0]:
                r = mid
            else:
                l = mid + 1
        return nums[l]