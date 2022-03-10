class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        from collections import Counter
        # counter
        nums_cnt = Counter(nums)
        # most frequent k
        result = nums_cnt.most_common(k)
        # extract only keys
        result_keys = [i for i, _ in result]
        
        return result_keys