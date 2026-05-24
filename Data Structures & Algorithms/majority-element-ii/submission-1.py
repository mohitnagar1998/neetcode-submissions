class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        countMap = {}
        requiredCount = len(nums) // 3

        for n in nums:
            if n in countMap:
                countMap[n] += 1
            else:
                countMap[n] = 1

        res = []
        for key, value in countMap.items():
            if value > requiredCount:
                res.append(key)

        return res
        