# 백준 2529번 부등호
# https://www.acmicpc.net/problem/2529

k = int(input())  
signs = input().split()  

results = []  
visited = [False] * 10  

def check(a, b, op):  
    if op == '<':
        return a < b
    else:
        return a > b

def backtrack(index, num_str):
    if index == k + 1:  
        results.append(num_str)
        return

    for i in range(10):
        if not visited[i]:
            if index == 0 or check(int(num_str[-1]), i, signs[index - 1]):
                visited[i] = True
                backtrack(index + 1, num_str + str(i))
                visited[i] = False

backtrack(0, '')

# 결과를 정렬해서 출력
results.sort()
print(results[-1])  # 최대
print(results[0])   # 최소
