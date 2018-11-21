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
    
# A faster solution:
# Note that it is sufficient to mark the numbers
# starting from j^2 as all the smaller multiples
# of p will have already been marked at that point.

class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0
        isprime = [True] * n
        isprime[:2] = [False, False]
            
        for j in range(2, int(n ** 0.5)+1):
            if not isprime[j]: continue
            isprime[j * j:n:j] = [False] * len(isprime[j * j:n:j])
        return sum(isprime)
