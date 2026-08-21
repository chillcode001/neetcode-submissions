class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] != ".":
                    if board[r][c] in rows[r] or board[r][c] in cols[c]:
                        return False
                    rows[r].add(board[r][c])
                    cols[c].add(board[r][c])

                    box_r = r//3
                    box_c = c//3
                    if board[r][c] in boxes[(box_r, box_c)]:
                        return False
                    boxes[(box_r, box_c)].add(board[r][c])
        
        return True