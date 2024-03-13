use std::convert::TryInto;
use std::f64;

impl Solution {
    pub fn pivot_integer(n: i32) -> i32 {
        let x = ((n * (n + 1)) as f64 / 2.0).sqrt();
        let c = x as i32;
        if (c as f64).eq(&x) {
            c
        } else {
            -1
        }
    }
}
