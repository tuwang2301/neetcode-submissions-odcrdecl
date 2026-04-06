class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def isValid(line: List[str]) -> bool:
            check = set()
            for l in line:
                if l in check and l != '.':
                    return False
                else:
                    check.add(l)
            return True

        for line in board:
            if not isValid(line):
                return False
            
        columns = list(zip(*board))

        for col in columns:
            if not isValid(col):
                return False

        sub_boxes = []
        for box_row in range(3):
            for box_col in range(3):
                sub_box = [
                    board[r][c]
                    for r in range(box_row*3, box_row*3 + 3)
                    for c in range(box_col*3, box_col*3 + 3)
                ]
                sub_boxes.append(sub_box)
        

        for sub in sub_boxes:
            if not isValid(sub):
                return False

        return True
            