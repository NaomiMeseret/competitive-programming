# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row_check = [set() for _ in range(9)]
        col_check = [set() for _ in range(9)]
        box_check = [set() for _ in range(9)]
        
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == ".":
                    continue
                
                box_index = (r // 3) * 3 + (c // 3)
                
                if num in row_check[r] or num in col_check[c] or num in box_check[box_index]:
                    return False
                
                row_check[r].add(num)
                col_check[c].add(num)
                box_check[box_index].add(num)
        
        return True
            
            