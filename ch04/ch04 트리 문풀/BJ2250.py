# 백준 2250번 트리의 높이와 너비
# https://www.acmicpc.net/problem/2250

import sys
sys.setrecursionlimit(10000)  # 깊은 트리 대비 재귀 제한 늘리기

n = int(sys.stdin.readline())
tree = {}
parent_check = [0] * (n + 1)  # 루트 찾기용

for _ in range(n):
    parent, left, right = map(int, sys.stdin.readline().split())
    tree[parent] = (left, right)
    if left != -1:
        parent_check[left] = 1
    if right != -1:
        parent_check[right] = 1

# 루트 노드 찾기
for i in range(1, n + 1):
    if parent_check[i] == 0:
        root = i
        break

# 레벨별 최소/최대 열번호 저장
level_min = dict()
level_max = dict()

# 중위 순회하면서 열 번호 기록
x = 1  # 현재 열 번호

def inorder(node, level):
    global x
    if node == -1:
        return
    left, right = tree[node]

    inorder(left, level + 1)

    # 현재 노드의 열 번호 저장
    if level not in level_min:
        level_min[level] = x
        level_max[level] = x
    else:
        level_min[level] = min(level_min[level], x)
        level_max[level] = max(level_max[level], x)
    x += 1

    inorder(right, level + 1)

inorder(root, 1)

# 너비가 가장 큰 레벨 찾기
max_level = 1
max_width = level_max[1] - level_min[1] + 1

for level in level_min:
    width = level_max[level] - level_min[level] + 1
    if width > max_width:
        max_level = level
        max_width = width
    elif width == max_width and level < max_level:
        max_level = level

print(max_level, max_width)
