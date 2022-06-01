class Solution:
    from collections import deque
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_val = [0] * len(nums)
        tmp = deque() 
        for i in range(len(nums)):
            while tmp and i - tmp[0] >= k:
                tmp.popleft()
            while tmp and nums[tmp[-1]] < nums[i]:
                tmp.pop()
            if tmp:
                max_val[i] = nums[tmp[-1]]
            else:
                max_val[i] = nums[i]
            tmp.append(i)
        print(max_val)
        return max_val[k - 1:]