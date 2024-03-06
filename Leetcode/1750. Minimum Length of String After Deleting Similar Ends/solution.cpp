class Solution {
public:
    int minimumLength(string s) {
        int l = 0, r = s.length() - 1;
        char cur = '\0';
        while (r > l) {
            if (s[l] == cur) {
                l++;
            } else if (s[r] == cur) {
                r--;
            } else if (s[l] == s[r]) {
                cur = s[l];
            } else {
                break;
            }
        }
        return (r == l && r > 0 && s[l] == s[l - 1]) ? 0 : r - l + 1;
    }
};
