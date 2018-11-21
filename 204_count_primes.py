class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        hash_map = [False for _ in range(n + 1)]
        prime_list = []
        
        for i in range(2, n):
            if hash_map[i]: continue
            prime_list.append(i)
            
            j = 0
            while j * i <= n:
                hash_map[j * i] = True
                j += 1
        return len(prime_list)
