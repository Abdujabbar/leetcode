class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_products = [1]
        right_products = [1]
        
        
        for num in nums:
            left_products.append(left_products[-1] * num)
        
        for num in nums[::-1]:
            right_products.append(right_products[-1] * num)
        
        right_products = right_products[::-1]
        
        ans = []
        
        for i in range(1, len(left_products)):
            ans.append(left_products[i - 1] * right_products[i])
        
        return ans