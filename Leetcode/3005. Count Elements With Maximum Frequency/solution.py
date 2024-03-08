class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums = Counter(nums)
        n = list(nums.values())
        m = max(n)
        return n.count(m) * m
