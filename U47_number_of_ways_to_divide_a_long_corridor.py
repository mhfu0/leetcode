class Solution:
    def numberOfWays(self, corridor: str) -> int:
        corridor = corridor.strip('P')
        ans = 1
        mod = int(1e9 + 7)
        count = 0
        k = 0
        for c in corridor:
            if count == 2:
                if c == 'P':
                    k = k + 1
                else:
                    ans = (ans * (k + 1)) % mod
                    k = 0
                    count = 0
            if c == 'S':
                count = count + 1
        if count != 2:
            ans = 0
        return ans
            
