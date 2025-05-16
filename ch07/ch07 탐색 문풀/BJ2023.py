# 백준 2023번 신기한 소수
# https://www.acmicpc.net/problem/2023

import sys, math

def is_prime(x):
    if x < 2:
        return False
    if x == 2:          
        return True
    if x % 2 == 0:      
        return False
    limit = int(math.sqrt(x))
    i = 3
    while i <= limit:
        if x % i == 0:
            return False
        i += 2           
    return True

def dfs(num, depth, target):
    if depth == target:   
        result.append(num)
        return
    for d in (1, 3, 7, 9):
        next_num = num * 10 + d
        if is_prime(next_num):
            dfs(next_num, depth + 1, target)

n = int(sys.stdin.readline().strip())   
result = []                             

for first in (2, 3, 5, 7):
    if n == 1:
        result.append(first)
    else:
        dfs(first, 1, n)

result.sort()
for val in result:
    print(val)
