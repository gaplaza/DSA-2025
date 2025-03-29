# 백준 1406번 에디터
# https://www.acmicpc.net/problem/1406

# input()보다 빨라야 함
import sys
input = sys.stdin.readline

# 이중 연결 리스트 클래스
class DNode:
    def __init__(self, data='', prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

# 에디터 클래스
class Editor:
    def __init__(self, initial_text):
        self.head = DNode()
        self.cursor = self.head

        for ch in initial_text:
            self.insert(ch)
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
    def get_result(self):
        result = []
        ptr = self.head.next
        while ptr:
            result.append(ptr.data)
            ptr = ptr.next
        return ''.join(result)

def main():
    initial_text = input().strip()
    m = int(input())

    editor = Editor(initial_text)

    for _ in range(m):
        command = input().strip()
        if command == 'L':
            editor.move_left()
        elif command == 'D':
            editor.move_right()
        elif command == 'B':
            editor.backspace()
        elif command.startswith('P'):
            _, x = command.split()
            editor.insert(x)

    print(editor.get_result())

# 실행
if __name__ == "__main__":
    main()
