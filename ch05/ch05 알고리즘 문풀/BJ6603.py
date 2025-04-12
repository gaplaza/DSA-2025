# 백준 6603번 로또
# https://www.acmicpc.net/problem/6603

import sys

def dfs(start, depth):
    if depth == 6:
        print(' '.join(map(str, path)))
        return

    for i in range(start, len(nums)):
        path.append(nums[i])
        dfs(i + 1, depth + 1)
        path.pop()

while True:
    line = sys.stdin.readline().strip()
    if line == "0":
        break

    parts = list(map(int, line.split()))
    k = parts[0]
    nums = parts[1:]

    path = []
    dfs(0, 0)
    print()
