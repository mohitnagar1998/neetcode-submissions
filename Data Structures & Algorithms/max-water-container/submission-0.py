class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        maxStorage = 0

        while l < r:
            minHeight = min(heights[l], heights[r])
            distance = r - l
            currStorage = minHeight * distance
            maxStorage = max(maxStorage, currStorage)

            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1

        return maxStorage
