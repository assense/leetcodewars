class Solution {
public:
    int maxFrequencyElements(std::vector<int>& nums) {
        std::unordered_map<int, int> freqMap;
        int maxFreq = 0;
        for (int num : nums) {
            maxFreq = std::max(maxFreq, ++freqMap[num]);
        }
        int count = 0;
        for (const auto& pair : freqMap) {
            if (pair.second == maxFreq) {
                count++;
            }
        }
        return count * maxFreq;
    }
};
