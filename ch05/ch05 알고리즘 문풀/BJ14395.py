# 백준 14395번 4연산
# https://www.acmicpc.net/problem/14395

from collections import deque

s, t = map(int, input().split())

if s == t:
    print(0)
    exit()

visited = set()
queue = deque()
queue.append((s, "")) 
visited.add(s)

while queue:
    now, ops = queue.popleft()

    for op in ['*', '+', '-', '/']:
        if op == '*':
            next_num = now * now
        elif op == '+':
            next_num = now + now
        elif op == '-':
            next_num = 0
        elif op == '/':
            if now == 0:
                continue
            next_num = 1

        if next_num > 10**9 or next_num in visited:
            continue

        if next_num == t:
            print(ops + op)
            exit()

        visited.add(next_num)
        queue.append((next_num, ops + op))

# 도달할 수 없는 경우
print(-1)
