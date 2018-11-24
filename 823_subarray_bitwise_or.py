

#O(n^2) solution
class Solution:
    def subarrayBitwiseORs(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        nums = len(A)
        hash_map = {}
        table = [[A[i] for i in range(nums)] for _ in range(nums)]
        
        for i in range(nums):
            for j in range(i, nums):
                if j != i:
                    table[i][j] |= table[i][j-1]
                if table[i][j] not in hash_map:
                    hash_map[table[i][j]] = 1
        return len(hash_map)
