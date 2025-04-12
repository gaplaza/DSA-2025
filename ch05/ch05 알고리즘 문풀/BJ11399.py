# 백준 11399번 ATM
# https://www.acmicpc.net/problem/11399

n = int(input())
times = list(map(int, input().split()))

times.sort()  

total = 0
current = 0

for t in times:
    current += t        
    total += current    

print(total)
