class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        c = s.count('1')
        return (c-1) * '1' + (len(s)-c) * '0' + '1'
