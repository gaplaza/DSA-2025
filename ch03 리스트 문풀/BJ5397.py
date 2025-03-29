# 백준 5397번 키로거
# https://www.acmicpc.net/problem/5397

# 이중 연결 리스트 클래스
class DNode:
    def __init__(self, data='', prev=None, next=None):
        self.data = data             
        self.prev = prev
        self.next = next

# 키로거 클래스
class KeyLoggerSimulator:
    def __init__(self):
        self.head = DNode()           
        self.cursor = self.head       

    # 노드(문자) 삽입
    def insert(self, ch):
        new_node = DNode(ch)
        new_node.prev = self.cursor
        new_node.next = self.cursor.next

        if self.cursor.next:
            self.cursor.next.prev = new_node
        self.cursor.next = new_node
        self.cursor = new_node       

    # 왼쪽으로 이동
    def move_left(self):
        if self.cursor.prev:
            self.cursor = self.cursor.prev

    # 오른쪽으로 이동
    def move_right(self):
        if self.cursor.next:
            self.cursor = self.cursor.next

    # 입력 위치 앞 글자 삭제
    def backspace(self):
        if self.cursor == self.head:
            return  
        to_delete = self.cursor
        prev_node = to_delete.prev
        next_node = to_delete.next

        prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        self.cursor = prev_node  

    # 최종 문자열 반환
    def get_text(self):
        result = []
        ptr = self.head.next
        while ptr:
            result.append(ptr.data)
            ptr = ptr.next
        return ''.join(result)

def main():
    t = int(input())
    for _ in range(t):
        line = input().strip()
        kl = KeyLoggerSimulator()
        for ch in line:
            if ch == '<':
                kl.move_left()
            elif ch == '>':
                kl.move_right()
            elif ch == '-':
                kl.backspace()
            else:
                kl.insert(ch)
        print(kl.get_result())

# 실행
if __name__ == "__main__":
    main()