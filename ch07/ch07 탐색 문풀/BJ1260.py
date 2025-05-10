# 백준 1260번 DFS와 BFS
# https://www.acmicpc.net/problem/1260

def dfs(v, graph, visited, order):
    visited[v] = True         
    order.append(v)           
    for nxt in graph[v]:       
        if not visited[nxt]:
            dfs(nxt, graph, visited, order)

def bfs(start, graph, visited, order):
    queue = [start]            
    visited[start] = True

    while queue:               
        v = queue.pop(0)       
        order.append(v)
        for nxt in graph[v]:
            if not visited[nxt]:
                visited[nxt] = True
                queue.append(nxt)

def main():
    import sys
    N, M, V = map(int, sys.stdin.readline().split())
    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        a, b = map(int, sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for adj in graph:
        adj.sort()             # 번호가 작은 것부터 방문하려고 정렬

    # DFS
    visited = [False] * (N + 1)
    dfs_order = []
    dfs(V, graph, visited, dfs_order)

    # BFS
    visited = [False] * (N + 1)
    bfs_order = []
    bfs(V, graph, visited, bfs_order)

    print(' '.join(map(str, dfs_order)))
    print(' '.join(map(str, bfs_order)))

if __name__ == "__main__":
    main()