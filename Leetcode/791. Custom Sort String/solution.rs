use std::collections::HashMap;
impl Solution {
    pub fn custom_sort_string(order: String, s: String) -> String {
        let mut counter: HashMap<char, usize> = HashMap::new();

        for ch in s.chars() {
            *counter.entry(ch).or_insert(0) += 1;
        }

        let mut ans = String::new();

        for ch in order.chars() {
            if let Some(count) = counter.remove(&ch) {
                ans.extend(std::iter::repeat(ch).take(count));
            }
        }

        for (ch, count) in counter {
            ans.extend(std::iter::repeat(ch).take(count));
        }

        ans
    }
}
