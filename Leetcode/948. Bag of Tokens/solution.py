class Solution:
    def minimumLength(self, s: str) -> int:
        l, r, cur = 0, len(s)-1, ''
        while r > l:
            if s[l] == cur:
                l += 1
            elif s[r] == cur:
                r -= 1
            elif s[l] == s[r]:
                cur = s[l]
            else:
                break
        return 0 if r == l > 0 and s[l] == s[l-1] else r-l+1
