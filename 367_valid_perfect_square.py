class Solution:
    # binary search
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        ans = False
        while l <= r:
            m = l + (r-l)//2
            if m * m == num:
                ans = True
                break
            elif m * m > num:
                r = m - 1
            else:
                l = m + 1
        return ans
