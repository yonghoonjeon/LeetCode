class Solution:
    def kthLargestNumber(self, nums: [str], k: int) -> str:
        # covert to str to int
        int_nums = [int(i) for i in nums]
        # sort by desc order
        int_nums.sort(reverse=True)
        # find k th largest element
        val = int_nums[k-1]
        
        return str(val)        