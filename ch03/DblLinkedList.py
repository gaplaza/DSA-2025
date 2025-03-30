class DblLinkedList:              
  def __init__(self):             # 생성자
    self.head = None              # head 선언 및 None으로 초기화

  def display(self, msg='DblLinkedList: '):
    print(msg, end=' ')
    ptr = self.head
    while ptr is not None:        
      print(ptr.data, end='<=>')            # 이중 연결이라서 이렇게 출력
      ptr = ptr.next                        # 링크를 따라 다음 노드로 이동
    print('None')                           # 마지막 노드의 링크는 None이므로 None 출력   

  def insert(self, pos, e):         # pos번째 노드에 e 삽입
    node = DNode(e)                 # 삽입할 노드 생성
    before = self.getNode(pos-1)    # pos-1번째 노드를 before에 저장
    if before == None:              # before가 None이면 맨 앞에 추가
      node.next = self.head         # node의 다음 노드가 현재의 헤드 노드를 가리키도록 함
      if node.next is not None:     
        node.next.prev = node       # 그 노드의 prev를 node로 수정함
      self.head = node              # 헤드 노드는 이제부터 새로 추가된 애임
    else:
      before.append(node)

  def delete(self, pos):            # pos번째 노드 삭제
    before = self.getNode(pos-1)    # pos-1번째 노드를 before에 저장
    if before == None:               # 삭제 대상이 맨 앞(head)인 경우
      before = self.head             # 삭제 대상 노드를 before에 임시로 저장 (리턴용)
      if self.head is not None:      # 빈 리스트일 때 삭제 요청이 들어오는 예외 처리
        self.head = self.head.next   # head를 다음 노드로 변경
        if self.head is not None:    # head가 None이 아니면
          self.head.prev = None      # head의 prev를 None으로 설정
      return before                  # 삭제된 노드 반환 
    else:
      return before.popNext()        # before 다음 노드를 삭제하고 삭제된 노드 반환
    

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
      
  def popNext(self):                 # self 다음 노드를 삭제하는 연산 
    node = self.next                 # 삭제할 노드를 node에 저장
    if node is not None:             # self의 next가 있으면 
      self.next = node.next          # 1) self의 next를 node의 next로 변경  
      if self.next is not None:      # 2) self의 next가 None이 아니면, 즉 다음 노드가 있으면
        self.next.prev = self        # self의 next의 prev를 self로 변경
    return node                      # 삭제된 노드(즉, self의 다음 노드) 반환