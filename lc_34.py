class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        l = 0
        r = len(nums) - 1
        # [...][target,..]
        while l < r:
            mid = (l + r) // 2
            if nums[mid] >= target:
                r = mid
            else:
                l = mid + 1
        if nums[l] == target:
            start = l
        else:
            return [-1, -1]
        r = len(nums) - 1
        # [target....target][...]
        while l < r:
            mid = (l + r + 1) // 2
            if nums[mid] <= target:
                l = mid
            else:
                r = mid - 1
        return [start, l]