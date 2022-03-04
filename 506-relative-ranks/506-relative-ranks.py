class Solution:
    def quicksort(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        pivot = arr[-1]
        left_arr, right_arr, pivot_arr = [], [], []
        for num in arr:
            if num > pivot:
                left_arr.append(num)
            elif num < pivot:
                right_arr.append(num)
            else:
                pivot_arr.append(num)
                
        return self.quicksort(left_arr) + pivot_arr + self.quicksort(right_arr)
        
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # declare list
        rank_placement = []
        # sorted ascending order
        sorted_score = self.quicksort(score)
        # scoring
        for i in range(len(score)):
            if score[i] == sorted_score[0]:
                rank_placement.append("Gold Medal")
            elif score[i] == sorted_score[1]:
                rank_placement.append("Silver Medal")
            elif score[i] == sorted_score[2]:
                rank_placement.append("Bronze Medal")
            else:
                sorted_score.index(score[i])
                rank_placement.append(str(sorted_score.index(score[i]) + 1))
        
        return rank_placement        