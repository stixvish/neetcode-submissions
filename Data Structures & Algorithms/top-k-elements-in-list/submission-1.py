class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        r = []
        # count how often each number appears
        hm = dict()
        for num in nums:
            if num not in hm.keys():
                hm[num] = 0
            hm[num] += 1
        # put numbers into buckets
        bucket = [[] for _ in range(len(nums))]
        for num in hm:
            bucket[hm[num] - 1].append(num)
        # list in reverse order
        for l in reversed(bucket):
            r.extend(l)
            if len(r) >= k:
                return r