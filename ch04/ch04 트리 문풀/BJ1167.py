# 백준 1167번 트리의 지름
# https://www.acmicpc.net/problem/1167

import sys
from collections import deque

input = sys.stdin.readline
V = int(input())
graph = [[] for _ in range(V + 1)]

for _ in range(V):
    data = list(map(int, input().split()))
    node = data[0]
    i = 1
    while data[i] != -1:
        neighbor = data[i]
        weight = data[i + 1]
        graph[node].append((neighbor, weight))
        i += 2

def bfs(start):
    visited = [-1] * (V + 1)
    queue = deque()
    queue.append(start)
    visited[start] = 0
    max_dist = 0
    max_node = start

    while queue:
        now = queue.popleft()
        for neighbor, cost in graph[now]:
            if visited[neighbor] == -1:
                visited[neighbor] = visited[now] + cost
                queue.append(neighbor)
                if visited[neighbor] > max_dist:
                    max_dist = visited[neighbor]
                    max_node = neighbor

    return max_node, max_dist

farthest_node, _ = bfs(1)
_, diameter = bfs(farthest_node)

print(diameter)
