class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap={}

        for i in range(len(nums)):
            dif=target-nums[i]
            if dif in prevMap:
                return [prevMap[dif],i]
            prevMap[nums[i]]=i
        return []


        