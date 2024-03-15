impl Solution {
    pub fn product_except_self(nums: Vec<i32>) -> Vec<i32> {
        let mut product = 1;
        let mut zeros = 0;

        for &num in &nums {
            if num == 0 {
                zeros += 1;
                if zeros == 2 {
                    return vec![0; nums.len()];
                }
            } else {
                product *= num;
            }
        }

        if zeros > 0 {
            nums.iter().map(|&num| if num != 0 { 0 } else { product }).collect()
        } else {
            nums.iter().map(|&num| product / num).collect()
        }
    }
}

