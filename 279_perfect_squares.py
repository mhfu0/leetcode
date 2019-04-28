class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(int(n ** 0.5) + 1):
            table[i * i] = 1
        for i in range(2, n + 1):
            if table[i] == 1: continue
            sqrt = int(i ** 0.5)
            for j in range(sqrt + 1):
                table[i] = min(table[i], table[i-j*j] + 1)
                if table[i] == 1: break
        return table[n]
        
