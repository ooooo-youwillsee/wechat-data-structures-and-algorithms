# coding=utf-8

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        rows = ['' for i in range(0, min(numRows, len(s)))]
        cur_row = 0
        goingDown = False
        for c in s:
            rows[cur_row] += c
            if cur_row == 0 or cur_row == numRows - 1:
                goingDown = not goingDown
            cur_row = cur_row + 1 if goingDown else cur_row - 1

        return ''.join(rows)


if __name__ == '__main__':
    s = Solution()
    print('LDREOEIIECIHNTSG')
    print(s.convert('LEETCODEISHIRING', 4))
    print(s.convert('ABCD', 3))
    print(s.convert('ABCDE', 4))
