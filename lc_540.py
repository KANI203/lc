class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        nums.append(10**5 + 1)
        l = 0
        r = len(nums) // 2
        # [(x1, x1)][(target, x2),(x2, x3)...(xn, 10^5 + 1)]
        # 2*i, 2*i + 1
        while l < r:
            mid = (l + r) // 2
            if nums[2 * mid] < nums[2 * mid + 1]:
                r = mid
            else:
                l = mid + 1
        return nums[2 * l]