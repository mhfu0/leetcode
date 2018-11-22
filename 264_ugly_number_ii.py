class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return n
        number_list = [1]
        count = 1
        p2, p3, p5 = 0, 0, 0
        while count < n:
            next_2 = number_list[p2] * 2
            next_3 = number_list[p3] * 3
            next_5 = number_list[p5] * 5
            next_min = min(next_2, next_3, next_5)
            if next_min == next_2:
                p2 += 1
            if next_min == next_3:
                p3 += 1
            if next_min == next_5:
                p5 += 1
            if not next_min in number_list:
                number_list.append(next_min)
                count += 1
        return number_list[-1]
