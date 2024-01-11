class Solution:
    def kthSmallest(self, matrix: [[int]], k: int) -> int:
        set_matrix = sorted([y for x in matrix for y in x])
        value = set_matrix[k-1]
        
        return value