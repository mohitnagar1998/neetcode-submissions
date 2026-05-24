class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        # find peak
        l, r = 1, length - 2
        while l <= r:
            m = (l + r) // 2
            left, mid, rigth = mountainArr.get(m - 1), mountainArr.get(m), mountainArr.get(m + 1)
            if left < mid < rigth:
                l = m + 1
            elif left > mid > rigth:
                r = m - 1
            else:
                break

        peak = m
        
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            if target > val:
                l = m + 1
            elif target < val:
                r = m - 1
            else:
                return m

        l, r = peak, length - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)
            if target < val:
                l = m + 1
            elif target > val:
                r = m - 1
            else:
                return m

        return -1




