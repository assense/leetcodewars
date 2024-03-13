class Solution {
public:
    int pivotInteger(int n) {
        double x = sqrt(n * (n + 1) / 2);
        int c = static_cast<int>(x);
        return (c == x) ? c : -1;
    }
};
