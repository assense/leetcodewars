class Solution:
    def customSortString(self, order: str, s: str) -> str:
        c = Counter(s)
        ans = ''
        for char in order:
            ans += char * counter[char]
            del counter[char]

        for char, count in counter.items():
            ans += char * count
        
        return ans
