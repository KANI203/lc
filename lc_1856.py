class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        # 前缀和
        prevSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prevSum[i + 1] = prevSum[i] + nums[i]
        # 左右索引
        leftStk = [0]
        l = [0] * len(nums)
        rightStk = [len(nums) - 1]
        r = [len(nums) - 1] * len(nums)
        for i in range(0,len(nums)):
            while leftStk and nums[leftStk[-1]] >= nums[i]:
                leftStk.pop()
            if leftStk:
                l[i] = leftStk[-1] + 1
            leftStk.append(i)
        for i in range(len(nums) - 1, -1, -1):
            while rightStk and nums[rightStk[-1]] >= nums[i]:
                rightStk.pop()
            if rightStk:
                r[i] = rightStk[-1] - 1
            rightStk.append(i)
        # 计算
        maxV = 0
        for i in range(len(nums)):
            prod = nums[i] * (prevSum[r[i] + 1] - prevSum[l[i]])
            maxV = max(maxV, prod)
        return maxV % (10 ** 9 + 7)