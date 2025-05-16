class BSTNode:                      # 이진 탐색 트리를 위한 노드 클래스
  def __init__ (self, key, value):  # 생성자: 키와 값을 받음
    self.key = key                  # 키(key)
    self.value = value              # 값(value): 키를 제외한 데이터 부분
    self.left = None                # 왼쪽 자식에 대한 링크
    self.right = None               # 오른쪽 자식에 대한 링크
    
def search_bst(n, key):
  if n == None:
    return None
  elif key == n.key:
    return n
  elif key < n.key:
    return search_bst(n.left, key)
  else:
    return search_bst(n.right, key)
  
def search_bst_iter(root, key):
    n = root                     # 현재 방문 노드
    while n is not None:         # 더 내려갈 노드가 없을 때까지
        if key == n.key:         # 일치 → 성공
            return n
        elif key < n.key:        # 더 작으면 왼쪽 서브트리로
            n = n.left
        else:                    # 더 크면 오른쪽 서브트리로
            n = n.right
    return None                  # 끝까지 못 찾으면 실패

def search_value_bst(n, value):
  if n == None: 
    return None
  elif value == n.value:
    return n
  res = search_value_bst(n.left, value)
  if res is not None:
    return res
  else:
    return search_value_bst(n.right, value)
  
def insert_bst(root, node):
  if root == None:
    return node
  
  if node.key == root.key:
    return root
  
  if node.key < root.key:
    root.left = insert_bst(root.left, node)
    
  else:
    root.right = insert_bst(root.right, node)
  
  return root