class Solution:
    def pivotInteger(self, n: int) -> int:
        x = math.sqrt(n * (n + 1) / 2)
        c = int(x)
        return c if c == x else -1
