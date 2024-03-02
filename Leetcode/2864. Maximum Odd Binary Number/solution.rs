impl Solution {
    pub fn maximum_odd_binary_number(s: String) -> String {
        let count_ones = s.chars().filter(|&c| c == '1').count();
        let result = "1".repeat(count_ones - 1) + &"0".repeat(s.len() - count_ones) + "1";
        result
    }
}
