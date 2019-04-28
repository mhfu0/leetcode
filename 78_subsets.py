# Top-down recursion. TLE with last test case
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def helper(nums):
            if nums not in res:
                res.append(nums)
            if not nums:
                return 
            for i in range(len(nums)):
                helper(nums[:i]+nums[i+1:])
        helper(nums)
        return res

# Bottom-up. AC, PR=67.61
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums: # len(nums) == 0
            return [[]]
        N = len(nums)
        res = [[], [nums[0]]]
        for i in range(1, N):
            new_s = []
            for s in res:
                new_s.append(s + [nums[i]])
            res += new_s
        return res
