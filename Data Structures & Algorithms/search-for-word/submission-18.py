class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()
        def exist (row, col, word):
            if row not in range(len(board)) or col not in range(len(board[0])):
                return False
            
            print(board[row][col], word)
            if board[row][col] != word[0]:
                return False

            if board[row][col] == word:
                return True

            if board[row][col] == word[0] and (row,col) not in visited:
                visited.add((row,col))
                neighbor = [(0,1), (1,0), (0,-1), (-1,0)]
                
                for n in neighbor:
                    n_id = (row + n[0], col + n[1])
                    if n_id in visited:
                        continue
                    check = exist(n_id[0], n_id[1], word[1:])
                    if check:
                        return True
                
                visited.remove((row,col))

                return False
                    

        
        row, col = len(board), len(board[0])

        for r in range(row):
            for c in range(col):
                if exist(r,c,word):
                    return True
        
        return False
