class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zeros = 0
        
        for num in nums:
            if num == 0:
                zeros += 1
                if zeros == 2:
                    return [0] * len(nums)
            else:
                product *= num
        
        if zeros:
            return [0 if num != 0 else product for num in nums]
        else:
            return [product // num for num in nums]
