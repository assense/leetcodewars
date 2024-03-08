impl Solution {
    pub fn max_frequency_elements(nums: Vec<i32>) -> i32 {
        let mut freq_map: HashMap<i32, i32> = HashMap::new();
        let mut max_freq = 0;
        for num in nums.iter() {
            max_freq = max_freq.max(*freq_map.entry(*num).or_insert(0) + 1);
        }
        let mut count = 0;
        for (_, &freq) in freq_map.iter() {
            if freq == max_freq {
                count += 1;
            }
        }
        count * max_freq
    }
}
