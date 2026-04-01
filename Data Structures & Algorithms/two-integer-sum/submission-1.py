class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        
        num_in = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_in:
                return [num_in[complement], i]
            num_in[num] = i