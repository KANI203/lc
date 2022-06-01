class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        # find mid in the none-decrease arrays
        def findTarget(l, r):
            # [...,][target, ...]
            # increase
            while l < r:
                mid = (l + r) // 2
                if nums[mid] >= target:
                    r = mid
                else:
                    l = mid + 1
            if nums[l] == target:
                return True
            else:
                return False

        # find the first smaller num in the right
        # divide into several none-decrease arrays
        i = 0
        while i < len(nums) - 1 and nums[i + 1] >= nums[i]:
            i += 1
        # single increased or maxid on the most right
        if i == len(nums) - 1:
            if target > nums[-1] or target < nums[0]:
                return False
            else:
                return findTarget(0, len(nums) - 1)
        else:
            maxId = i
            # print(maxId)
            if target > nums[maxId] or target < nums[maxId + 1]:
                return False
            elif target < nums[0]:
                return findTarget(maxId + 1, len(nums) -1) 
            elif target >= nums[0]:
                return findTarget(0, maxId)