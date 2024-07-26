class Solution:
    def majorityElement(self, nums: List[int]) -> int:    
        count = Counter(nums)
        n = (len(nums)//2) + 1
        for i in count:
            if count[i] >= n:
                num = i
        return num