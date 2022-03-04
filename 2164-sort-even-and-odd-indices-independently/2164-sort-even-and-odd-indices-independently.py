class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        # declare list
        result = nums
        odds = []
        odd_indices = []
        even = []
        even_indices = []
        # loop check
        for i in range(len(nums)):
            if i % 2 == 1:
                odds.append(nums[i])
                odd_indices.append(i)
            else:
                even.append(nums[i])
                even_indices.append(i)
        # sort
        odds_sorted = sorted(odds, reverse=True)
        even_sorted = sorted(even)
        # replace
        for j in range(len(odd_indices)):
            result[odd_indices[j]] = odds_sorted[j]
        for k in range(len(even_indices)):
            result[even_indices[k]] = even_sorted[k]
        
        return result
        