Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
Example 2:

Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
    
    
    
    def runningSum(self, nums: List[int]) -> List[int]:
        new = [0]*len(nums)
        for i in range(len(nums)):
            new[i] = nums[i] + sum(nums[:i])
        return new
