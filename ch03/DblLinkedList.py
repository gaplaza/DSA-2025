class DNode:
  def __init__(self, elem, prev=None, link=None):
    self.data = elem        # 노드의 데이터 필드 멤버 생성 및 초기화
    self.prev = prev        # 이전 노드 링크 생성 및 초기화
    self.link = link        # 다음 노드 링크 생성 및 초기화
  
  def append(self, node):         # self 다음에 node를 넣는 연산
    if node is not None:          # 삽입할 node가 None이 아니면 1), 2) 단계를 통해 node를 다음 노드로 연결
      node.next = self.next       # 1)
      node.prev = self            # 2)
      if node.next is not None:   # 3) self 다음 노드가 있으면 그 노드의 이전 노드는 Node
        node.next.prev = node     
      self.next = node            # 4) 