class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        bottom = 0
        top = len(matrix) - 1

        while bottom <= top:
            midRow = (bottom + top) // 2

            if target < matrix[midRow][0]:
                top = midRow - 1
            elif matrix[midRow][len(matrix[0]) - 1]:
                bottom = midRow + 1
            else: # target in matrix[midRow]
                l = 0
                r = len(matrix[midRow]) - 1

                while l <= r:
                    midCol = (l + r) // 2

                    if target < matrix[midRow][midCol]:
                        r = midCol - 1
                    elif target > matrix[midRow][midCol]:
                        l = midCol + 1
                    else: # target == matrix[midRow][midCol]
                        return True
        
        return False