class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        joinedlist = nums1 + nums2
        joinedlist = sorted(joinedlist)
        if (m + n) % 2 == 0:
            median =  (joinedlist[int((m+n)/2) - 1] + joinedlist[int((m+n)/2)]) / 2
        else:
            median = joinedlist[((m+n)//2)]
        return median