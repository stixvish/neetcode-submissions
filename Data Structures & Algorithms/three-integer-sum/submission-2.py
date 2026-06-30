class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for a in range(0, len(nums)):
            if nums[a] == nums[a-1] and a != 0:
                continue
            t = nums[a] * -1
            b = a + 1
            c = len(nums) - 1
            while True:
                if b >= c:
                    break
                if nums[b] + nums[c] == t:
                    ans.append([nums[a], nums[b], nums[c]])
                    b += 1
                    while b < c and nums[b] == nums[b-1]:
                        b += 1
                elif nums[b] + nums[c] > t:
                    c -= 1
                elif nums[b] + nums[c] < t:
                    b += 1
        return ans