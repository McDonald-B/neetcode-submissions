class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}
        for i in range(len(nums)):
            requiredValue = target - nums[i]
            if requiredValue in hashmap:
                return [hashmap[requiredValue], i]
            hashmap[nums[i]] = i
        return []
        