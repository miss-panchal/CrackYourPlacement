class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums.sort()
        ans = []
        for i in range(0,len(nums)-1):
            if nums[i] == nums[i+1]:
                ans.append(nums[i])
        return ans