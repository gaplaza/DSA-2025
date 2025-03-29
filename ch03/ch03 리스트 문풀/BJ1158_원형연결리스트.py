# 백준 1158번 요세푸스 문제
# https://www.acmicpc.net/problem/1158

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def main():
    n, k = map(int, input().split())

    head = Node(1)
    prev = head
    for i in range(2, n + 1):
        node = Node(i)
        prev.next = node
        prev = node
    prev.next = head     

    result = []
    curr = head
    before = prev        

    while n > 0:
        for _ in range(k - 1):      
            before = curr
            curr = curr.next

        result.append(curr.data)
        before.next = curr.next     
        curr = curr.next
        n -= 1

    print(f"<{', '.join(map(str, result))}>")

# 실행
if __name__ == "__main__":
    main()
