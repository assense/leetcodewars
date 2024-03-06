impl Solution {
    pub fn minimum_length(s: String) -> i32 {
        let mut l = 0;
        let mut r = s.len() - 1;
        let mut cur: char = '\0';
        while r > l {
            if s.chars().nth(l).unwrap() == cur {
                l += 1;
            } else if s.chars().nth(r).unwrap() == cur {
                r -= 1;
            } else if s.chars().nth(l).unwrap() == s.chars().nth(r).unwrap() {
                cur = s.chars().nth(l).unwrap();
            } else {
                break;
            }
        }
        if r == l && r > 0 && s.chars().nth(l).unwrap() == s.chars().nth(l - 1).unwrap() {
            return 0;
        } else {
            return (r - l + 1) as i32;
        }
    }
}
