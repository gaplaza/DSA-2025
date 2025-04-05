import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from ch02.ArrayQueue import ArrayQueue

class BTNode:
  def __init__(self, elem, left=None, right=None):
    self.data = elem
    self.left = left
    self.right = right
  def isLeaf(self):
    return self.left is None and self.right is None

def inorder(n):
  if n is not None:
    inorder(n.left)
    print(n.data, end=' ')
    inorder(n.right)

def preorder(n):
  if n is not None:
    print("( ", end='')         # 열기
    print(n.data, end=' ')
    preorder(n.left)
    preorder(n.right)
    print(") ", end='')         # 닫기

def postorder(n):
  if n is not None:
    postorder(n.left)
    postorder(n.right)
    print(n.data, end=' ')

def levelorder(root):
  queue = ArrayQueue()
  queue.enqueue(root)
  while not queue.isEmpty():
    n = queue.dequeue()
    if n is not None:
      print(n.data, end=' ')
      queue.enqueue(n.left)
      queue.enqueue(n.right)

def count_node(n):
  if n is None:
    return 0
  return count_node(n.left) + count_node(n.right) + 1

def calc_height(n):
  if n is None:
    return 0
  hLeft = calc_height(n.left)
  hRight = calc_height(n.right)
  return max(hLeft, hRight) + 1

# 🔻 여기부터 메인 함수로 감싸기
def main():
  # 트리 구성
  d = BTNode('D')
  e = BTNode('E')
  b = BTNode('B', d, e)
  f = BTNode('F')
  c = BTNode('C', f, None)
  root = BTNode('A', b, c)

  # 실행
  print('\nIn-Order : ', end=''); inorder(root)
  print('\nPre-Order : ', end=''); preorder(root)
  print('\nPost-Order : ', end=''); postorder(root)
  print('\nLevel-Order : ', end=''); levelorder(root)
  print()

  print("노드의 개수 = %d개" % count_node(root))
  print("트리의 높이 = %d" % calc_height(root))

# 🔻 다른 파일에서 import 될 때는 main() 실행 X
if __name__ == "__main__":
  main()
