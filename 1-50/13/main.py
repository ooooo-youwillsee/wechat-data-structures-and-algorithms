# coding=utf-8


class Solution:

    def __init__(self) -> None:
        self.count = 0

    def solution(self, n):
        print(self.help(0, 0, n, n))

    def help(self, x, y, targetX, targetY):
        i = 0
        if x == targetX and y == targetY:
            i += 1
        if x < targetX:
            i += self.help(x + 1, y, targetX, targetY)
        if y < targetY:
            i += self.help(x, y + 1, targetX, targetY)
        return i


if __name__ == '__main__':
    s = Solution()
    s.solution(2)
