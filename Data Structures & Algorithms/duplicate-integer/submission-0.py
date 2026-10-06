class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()     #O(logn)
        for i in range(1,len(nums)): #O(n)
            if nums[i-1]==nums[i]:
                return True

        return False        

    #O(nlogn)