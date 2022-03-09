class Solution:
    def euclide_distance(self, point: [int]) -> [int]:
        """
        Compute the Euclidean distance from the zero points(0, 0), and return it.
        """
        import numpy as np
        
        # declare x, y
        x = point[0]
        y = point[1]
        
        # compute euclidean distance
        dist = np.sqrt((x**2) + (y**2))
        
        return dist
        
    def kClosest(self, points: [[int]], k: int) -> [[int]]:
        # sorted
        points.sort(key=self.euclide_distance)
        
        # pick k
        return points[:k]
        