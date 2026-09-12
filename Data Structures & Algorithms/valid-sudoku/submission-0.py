class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        N = 9

        # check rows
        for row in board:
            seen = set()
            for x in range(N):
                if row[x] == ".":
                    continue
                if row[x] in seen:
                    return False
                seen.add(row[x])

        # check cols
        for x in range(N):
            seen = set()
            for y in range(N):
                char = board[y][x]
                if char == ".":
                    continue
                if char in seen:
                    return False
                seen.add(char)

        # check 3x3
        for ly in range(0, N, 3):
            for lx in range(0, N, 3):
                seen = set()
                for y in range(ly, ly+3):
                    for x in range(lx, lx+3):
                        char = board[y][x]
                        if char == ".":
                            continue
                        if char in seen:
                            return False
                        seen.add(char)
        
        return True