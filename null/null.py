class Solution:
    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # element check
        if len(nums1) > m:
            # get 0 indices
            indexes = [i for i, val in enumerate(nums1) if val == 0]
            # insert
            for i in range(n):
                nums1[indexes[i]] = nums2[i]
        else:
            pass
        # sort
        nums1.sort()