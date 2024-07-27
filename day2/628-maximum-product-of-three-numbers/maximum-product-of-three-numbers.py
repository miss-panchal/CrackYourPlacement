class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # Sort the array in ascending order
        nums.sort()
        
        # The maximum product can be from either:
        # 1. The product of the three largest numbers
        # 2. The product of the two smallest (most negative) numbers and the largest number
        max_product1 = nums[-1] * nums[-2] * nums[-3]
        max_product2 = nums[0] * nums[1] * nums[-1]
        
        # Return the maximum of the two products
        return max(max_product1, max_product2)