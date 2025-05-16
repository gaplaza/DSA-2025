# 백준 13023번 ABCDE
# https://www.acmicpc.net/problem/13023

import sys

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N)]  
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * N
found = False                  

# DFS
def dfs(node, depth):
    global found

    if found:                  
        return
    if depth == 4:             
        found = True
        return

    visited[node] = True
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, depth + 1)
    visited[node] = False     

for i in range(N):
    dfs(i, 0)
    if found:
        break

if found:
    print(1)
else:
    print(0)
