class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        curr_sum = 0
        
        for num in nums:
            if curr_sum < 0:
                curr_sum = 0
            curr_sum += num
            max_sum = max(max_sum, curr_sum)
        
        return max_sum