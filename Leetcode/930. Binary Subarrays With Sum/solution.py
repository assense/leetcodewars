class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        s = 0
        c = Counter({0: 1})
        for i in nums:
            s += i
            res += c[s - goal]
            c[s] += 1
        return res
