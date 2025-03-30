class LinkedList:             # 단순 연결 리스트 클래스
  def __init__(self):         # 생성자
    self.head = None          # 헤드 선언 및 None으로 초기화 
  def isEmpty(self):          # 공백 상태 검사
    return self.head == None  # 헤드가 None이면 공백
  def isFull(self):           # 포화 상태 검사
    return False              # 연결 리스트는 포화 상태가 아님
  
  def getNode(self, pos):
    if pos < 0:              # 위치가 음수이면 그런 노드가 없음 -> None 반환
      return None
    ptr = self.head          # 시작 위치는 헤드
    for i in range(pos):     # 머리 노드에서부터 링크를 따라 pos번 이동하면 pos 위치의 노드에 도착
      if ptr == None:
        return None          
      ptr = ptr.link         # 다음 노드로 이동
    return ptr               # 최종 위치에 해당하는 노드 반환
  
  def getEntry(self, pos):
    node = self.getNode(pos)  # pos번째 노드 반환
    if node == None:          # 해당 노드가 없는 경우
      return None
    else:
      return node.data        # 노드의 데이터 필드 반환
    
  def insert(self, pos, e):
    node = Node(e, None)            # 삽입할 노드 생성
    before = self.getNode(pos-1)    # pos-1번째 노드를 before에 저장
    if before == None:              # before가 None이면 맨 앞에 추가
      node.link = self.head         # node의 링크가 헤드 노드를 가리키도록 함
      self.head = node              # 헤드 노드는 이제부터 새로 추가된 애임
    else:
      before.append(node)           # before 다음에 node를 삽입
  
  def delete(self, pos):
    before = self.getNode(pos-1)       # pos-1번째 노드를 before에 저장
    if before == None:                 # 삭제 대상이 맨 앞(head)인 경우
      before = self.head               # 삭제 대상 노드를 before에 임시로 저장 (리턴용)
      if self.head is not None:        # 빈 리스트일 때 삭제 요청이 들어오는 예외 처리
        self.head = self.head.link     # head를 다음 노드로 변경
      return before                    # 삭제된 노드 반환 
    else:
      return before.popNext()          # before 다음 노드를 삭제하고 삭제된 노드 반환
    
  def size(self):
    ptr = self.head
    count = 0
    while ptr is not None:
      ptr = ptr.link                 # 링크를 따라 ptr이 이동
      count += 1
    return count                     # 노드 개수 반환
  
  def display(self, msg='LinkedList: '):
    print(msg, end=' ')
    ptr = self.head
    while ptr is not None:         # 링크를 따라 ptr이 이동
      print(ptr.data, end='->')    # ptr의 데이터 출력
      ptr = ptr.link
    print('None')                  # 마지막 노드의 링크는 None이므로 None 출력
  
class Node:
  def __init__(self, elem, link=None):
    self.data = elem        # 데이터 멤버 생성 및 초기화
    self.link = link        # 링크 생성 및 초기화
  def append(self, node):   # self 다음에 node를 넣는 연산
    if node is not None:    # 삽입할 node가 None이 아니면 1), 2) 단계를 통해 node를 다음 노드로 연결
      node.link = self.link
      self.link = node
  def popNext (self):          # self 다음 노드를 삭제하는 연산
    next = self.link           # self의 다음 노드를 next에 저장
    if next is not None:       # next가 None이 아니면 2)단계 처리
      self.link = next.link
    return next                # 다음 노드를 반환