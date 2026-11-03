# LeetCode 36. Valid Sudoku (NeetCode 150)
# https://leetcode.com/problems/valid-sudoku/
# Difficulty: Medium
# Pattern: arrays-hashing
# Time: O(1)  Space: O(1)  (the board is always 9x9, so 81 cells)
# Two versions below: Solution (single pass, improved) and SolutionThreePasses (first
# attempt, kept for comparison; rename it to Solution to submit).
# Insight:
#   - Why it works: the board is valid iff no digit repeats in any row, column or
#     3x3 box. Each cell is checked against three sets (rows[r], cols[c],
#     boxes[(r // 3, c // 3)]) and added to them, and set lookups are O(1).
#   - Improved over the three-pass version: one scan of the 81 cells instead of three
#     separate scans, and it returns False at the first repeat instead of building
#     every list and comparing lengths afterwards. (r // 3, c // 3) identifies the box
#     directly, replacing the four nested loops and the 3 * i + k offset arithmetic.
#   - [PYTHONIC] defaultdict(set) removes the "if key not in dict" setup, and the tuple
#     (r // 3, c // 3) works as a dict key.
#   - [PYTHONIC] len(els) != len(set(els)) is the quick duplicate check (same as 217).
#   - [PYTHONIC] zip(*board) transposes the board, so the column pass becomes
#         for col in zip(*board): ...
#     instead of indexing row[i] for every row.
#   - Alternative: one set of tagged tuples instead of three dicts of sets, e.g.
#     seen.add(("row", r, v)), ("col", c, v), ("box", r // 3, c // 3, v), and return
#     False if any is already in seen.

from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                value = board[r][c]
                if value == ".":
                    continue
                box = (r // 3, c // 3)
                if value in rows[r] or value in cols[c] or value in boxes[box]:
                    return False
                rows[r].add(value)
                cols[c].add(value)
                boxes[box].add(value)

        return True


class SolutionThreePasses:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            els = [x for x in row if x.isdigit()]
            if len(els)!=len(set(els)):
                return False
        for i in range(len(board)):
            els = [row[i] for row in board if row[i].isdigit()]
            if len(els)!=len(set(els)):
                return False
        for i in range(3):
            for j in range(3):
                els = []
                for k in range(3):
                    for l in range(3):
                        if board[3*i+k][3*j+l].isdigit():
                            els.append(board[3*i+k][3*j+l])
                if len(els)!=len(set(els)):
                    return False
        return True
