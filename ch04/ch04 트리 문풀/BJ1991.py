# 백준 1991번 트리 순회
# https://www.acmicpc.net/problem/1991

n = int(input())
tree = {}

for i in range(n):
  parent, left, right = input().split()
  tree[parent] = [left, right]
  
def preorder(node):
  result.append(node)
  left, right = tree[node]
  if left != '.':
    preorder(left)
  if right != '.':
    preorder(right)

def inorder(node):
  left, right = tree[node]
  if left != '.':
    inorder(left)
  result.append(node)
  if right != '.':
    inorder(right)
    
def postorder(node):
  left, right = tree[node]
  if left != '.':
    postorder(left)
  if right != '.':
    postorder(right)
  result.append(node)

result = []
preorder('A')
print(''.join(result))     # 원래 리스트 형태로 나오니까 각 요소 사이에 아무 것도 붙이지 않고 이어붙이기

result = []
inorder('A')
print(''.join(result))

result = []
postorder('A')
print(''.join(result))