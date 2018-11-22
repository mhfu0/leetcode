class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 0: return False
        fac = [2, 3, 5]
        for f in fac:
            while (num % f) == 0:
                num /= f
        return True if num == 1 else False
