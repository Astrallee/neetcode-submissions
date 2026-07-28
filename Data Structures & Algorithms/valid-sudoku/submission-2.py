class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                num = board[r][c]

                # 空格跳过
                if num == ".":
                    continue

                # 当前3x3区域编号
                box_id = (r // 3) * 3 + (c // 3)

                # 检查重复
                if num in rows[r]:
                    return False

                if num in cols[c]:
                    return False

                if num in boxes[box_id]:
                    return False

                # 加入记录
                rows[r].add(num)
                cols[c].add(num)
                boxes[box_id].add(num)

        return True
        