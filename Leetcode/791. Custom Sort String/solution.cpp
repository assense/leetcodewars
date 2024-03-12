class Solution {
public:
    string customSortString(string order, string s) {
        unordered_map<char, int> counter;
        for (char ch : s) {
            counter[ch]++;
        }
        
        string ans = "";
        for (char ch : order) {
            if (counter.find(ch) != counter.end()) {
                ans.append(counter[ch], ch);
                counter.erase(ch);
            }
        }
        
        for (auto& pair : counter) {
            ans.append(pair.second, pair.first);
        }
        
        return ans;
    }
};
