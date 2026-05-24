class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rotateArray(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        k = k % len(nums)
        rotateArray(0, len(nums) - 1)
        rotateArray(0, k - 1)
        rotateArray(k, len(nums) - 1)
