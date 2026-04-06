class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1

        valid = - 1

        while left <= right:
            mid = left + (right - left)//2
            boundaries = [matrix[mid][0], matrix[mid][-1]]
            print(boundaries)

            if boundaries[0] <= target <= boundaries[1]:
                valid = mid
                break
            elif target > boundaries[1]:
                left = mid + 1
            else:
                right = mid - 1

        if valid == -1:
            return False
        else:
            box = matrix[valid]
            l, r = 0, len(box) - 1
            while l <= r:
                mid = l + (r - l)//2
                print(box[mid])
                if box[mid] == target:
                    return True
                elif box[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return False