class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        def canSplit(largest):
            currSum = 0
            subArray = 0

            for num in nums:
                currSum += num
                if currSum > largest:
                    subArray += 1
                    currSum = num
            
            return subArray + 1 <= k

        l, r = max(nums), sum(nums)
        res = r

        while l <= r:
            m = (l + r) // 2
            if canSplit(m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res