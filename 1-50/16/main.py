# coding=utf-8

class Solution:

    def solution(self, line, row, arr):
        if line < len(arr) and row < len(arr[line]):
            left = self.solution(line + 1, row, arr)
            right = self.solution(line + 1, row + 1, arr)
            if right > left:
                return arr[line][row] + right
            return arr[line][row] + left
        return 0


if __name__ == '__main__':
    arr = [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3],
    ]
    s = Solution()
    print(s.solution(0, 0, arr))
