class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        sizeOfArray = len(nums)
        for index in range(sizeOfArray):
            if nums[index] <= 0 or nums[index] > sizeOfArray:
                nums[index] = sizeOfArray + 1

        for i in range(sizeOfArray):
            val = abs(nums[i])
            if 1 <= val <= sizeOfArray:
                nums[val - 1] = -abs(nums[val - 1])

        for i in range(sizeOfArray):
            if nums[i] > 0:
                return i + 1

        return sizeOfArray + 1
