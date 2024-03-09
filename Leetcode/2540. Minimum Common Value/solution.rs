impl Solution {
    pub fn get_common(nums1: Vec<i32>, nums2: Vec<i32>) -> i32 {
        let mut i = 0;
        let mut j = 0;
        while i < nums1.len() && j < nums2.len() {
            if nums1[i] == nums2[j] {
                return nums1[i];
            }
            if nums1[i] > nums2[j] {
                j += 1;
            } else {
                i += 1;
            }
        }
        -1
    }
}
