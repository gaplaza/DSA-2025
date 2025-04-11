# 백준 11725번 트리의 부모 찾기
# https://www.acmicpc.net/problem/11725

import sys
sys.setrecursionlimit(1000000)  # 깊은 트리 대응

n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

# 양방향 간선 정보 저장
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

# DFS 탐색 (1번 노드를 루트로)
def dfs(node, par):
    for neighbor in graph[node]:
        if parent[neighbor] == 0:  # 아직 방문 안 한 노드
            parent[neighbor] = node
            dfs(neighbor, node)

dfs(1, 0)

# 2번 노드부터 출력
for i in range(2, n + 1):
    print(parent[i])
