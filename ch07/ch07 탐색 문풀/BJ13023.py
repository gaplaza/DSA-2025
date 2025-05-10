# 백준 13023번 ABCDE
# https://www.acmicpc.net/problem/13023

import sys

def main() -> None:
    N, M = map(int, sys.stdin.readline().split())
    g = [[] for _ in range(N)]
    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        g[a].append(b)
        g[b].append(a)

    visited = [False] * N
    found = False

    def dfs(v: int, depth: int) -> None:
        nonlocal found
        if found:                 
            return
        if depth == 4:            
            found = True
            return
        visited[v] = True
        for nxt in g[v]:
            if not visited[nxt]:
                dfs(nxt, depth + 1)
        visited[v] = False        

    for i in range(N):
        dfs(i, 0)
        if found:
            break

    print(1 if found else 0)

if __name__ == "__main__":
    main()
