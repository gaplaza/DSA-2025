# 백준 1300번 K번째 수
# https://www.acmicpc.net/problem/1300

import sys

def main() -> None:
    input = sys.stdin.readline
    N = int(input())
    k = int(input())

    lo, hi = 1, k

    # ‘mid 이하의 값이 몇 개인가’를 세어 k와 비교
    while lo < hi:
        mid = (lo + hi) // 2
        cnt = 0
        for i in range(1, N + 1):
            cnt += min(mid // i, N)   
        if cnt >= k:
            hi = mid                
        else:
            lo = mid + 1             
    print(lo)

if __name__ == "__main__":
    main()