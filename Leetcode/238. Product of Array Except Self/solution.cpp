class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int product = 1;
        int zeros = 0;

        for (int num : nums) {
            if (num == 0) {
                zeros++;
                if (zeros == 2) {
                    return std::vector<int>(nums.size(), 0);
                }
            } else {
                product *= num;
            }
        }

        if (zeros) {
            std::vector<int> result;
            for (int num : nums) {
                result.push_back((num != 0) ? 0 : product);
            }
            return result;
        } else {
            std::vector<int> result;
            for (int num : nums) {
                result.push_back(product / num);
            }
            return result;
        }
    }
};
