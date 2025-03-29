# 백준 1158번 요세푸스 문제
# https://www.acmicpc.net/problem/1158

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# 단일 연결 리스트 클래스
class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node
        self.size += 1

    # k번째 노드 삭제
    def remove(self, k):
        if self.size == 0:
            return None

        if k == 1:
            removed_value = self.head.value
            self.head = self.head.next
            self.size -= 1
            return removed_value

        prev = self.head
        for _ in range(k - 2):
            prev = prev.next
        removed = prev.next
        removed_value = removed.value
        prev.next = removed.next
        self.size -= 1
        return removed_value

    def __len__(self):
        return self.size

def main():
    n, k = map(int, input().split())
    lst = SinglyLinkedList()
    for i in range(1, n + 1):
        lst.append(i)

    result = []
    idx = 1 
    while len(lst) > 0:
        idx = (idx + k - 2) % len(lst) + 1  
        result.append(lst.remove(idx))

    print("<" + ", ".join(map(str, result)) + ">")

if __name__ == "__main__":
    main()
