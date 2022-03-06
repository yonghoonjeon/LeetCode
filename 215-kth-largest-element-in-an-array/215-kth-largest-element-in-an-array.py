class Solution:
    def findKthLargest(self, nums: [int], k: int) -> int:
        # sorted list
        sorted_nums = sorted(nums, reverse=True)
        # find k-th largest element
        kth_element = sorted_nums[k-1]
        
        return kth_element