# 백준 1158번 요세푸스 문제
# https://www.acmicpc.net/problem/1158

class DNode:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# 이중 원형 연결 리스트 클래스
class DoublyCircularLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # 노드 추가
    def append(self, value):
        new_node = DNode(value)
        if self.head is None:
            self.head = new_node
            new_node.prev = new_node
            new_node.next = new_node
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node
        self.size += 1

    # 노드 삭제
    def remove(self, node):
        if self.size == 0:
            return
        if self.size == 1:
            self.head = None
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
            if node == self.head:
                self.head = node.next
        self.size -= 1

    def __len__(self):
        return self.size


def main():
    n, k = map(int, input().split())
    cll = DoublyCircularLinkedList()

    for i in range(1, n + 1):
        cll.append(i)

    result = []
    current = cll.head

    while len(cll) > 0:
        for _ in range(k - 1):
            current = current.next
        result.append(current.value)
        next_node = current.next
        cll.remove(current)
        current = next_node

    print("<" + ", ".join(map(str, result)) + ">")


if __name__ == "__main__":
    main()
