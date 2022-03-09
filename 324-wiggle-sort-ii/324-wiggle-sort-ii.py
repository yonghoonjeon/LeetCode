class Solution:
    def wiggleSort(self, nums: [int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # sorted list
        sorted_nums = sorted(nums)
        # partition
        if len(nums) % 2 == 0:
            left = sorted_nums[:len(nums)//2]
            right = sorted_nums[len(nums)//2:]
        else:
            left = sorted_nums[:len(nums)//2+1]
            right = sorted_nums[len(nums)//2+1:]
        # reverse order
        left.reverse()
        right.reverse()
        # reassign values
        nums[::2] = left
        nums[1::2] = right