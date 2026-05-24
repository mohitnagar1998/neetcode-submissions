class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        numSet = set(nums)
        missingNumber = 1
        for i in range(len(nums)):
            if missingNumber not in numSet:
                return missingNumber
            missingNumber += 1
        return missingNumber