class Solution:
    def sortArray(self, nums: [int]) -> [int]:
        def merge(low: int, mid: int, high: int, L: list) -> None:
            temp = []
            l, h = low, mid

            while l < mid and h < high:
                if L[l] < L[h]:
                    temp.append(L[l])
                    l += 1
                else:
                    temp.append(L[h])
                    h += 1

            while l < mid:
                temp.append(L[l])
                l += 1
            while h < high:
                temp.append(L[h])
                h += 1

            for i in range(low, high):
                L[i] = temp[i - low]
                
        def sort(low, high):
            if high - low < 2:
                return
            mid = (low + high) // 2
            sort(low, mid)
            sort(mid, high)
            merge(low, mid, high, nums)

        sort(0, len(nums))
        
        return nums