class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if (len(nums) == 2):
            return [0, 1]
        hm = dict()
        for index, num in enumerate(nums):
            if num in hm.keys():
                return [hm[num], index]
            hm[target-num] = index