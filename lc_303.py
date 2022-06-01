class NumArray:
    def __init__(self, nums: List[int]):
        ans = [0] 
        for i in range(1, len(nums) + 1):
            ans.append(ans[i - 1] + nums[i - 1])
        self.ans = ans
    def sumRange(self, left: int, right: int) -> int:
        return self.ans[right + 1] - self.ans[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)