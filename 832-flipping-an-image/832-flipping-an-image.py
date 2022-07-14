from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        temp: List[[List[int]]] = []
        # flip each row
        for row in image:
            flipped_row: List[int] = []
            for i in range(len(row)):
                flipped_row.append(row[-(i+1)])
            temp.append(flipped_row)
        # reverse each row
        for i in range(len(temp)):
            row = temp[i]
            for j in range(len(row)):
                if temp[i][j] == 0:
                    temp[i][j] = 1
                else:
                    temp[i][j] = 0

        return temp
        