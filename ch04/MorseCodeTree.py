from BinaryTree import BTNode 

table = [
    ('A', '.-'),   ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
    ('E', '.'),    ('F', '..-.'), ('G', '--.'),  ('H', '....'),
    ('I', '..'),   ('J', '.---'), ('K', '-.-'),  ('L', '.-..'),
    ('M', '--'),   ('N', '-.'),   ('O', '---'),  ('P', '.--.'),
    ('Q', '--.-'), ('R', '.-.'),  ('S', '...'),  ('T', '-'),
    ('U', '..-'),  ('V', '...-'), ('W', '.--'),  ('X', '-..-'),
    ('Y', '-.--'), ('Z', '--..')
]

def encode(ch):
  idx = ord(ch) - ord('A')    # 리스트에서 해당 문자의 인덱스 ex) A는 0, B는 1, C는 2 ...
  return table[idx][1]        # 해당 문자의 모스 부호 반환

def decode_simple(morse):
  for tp in table:            # 모스 코드 표의 모든 문자에 대해 
    if morse == tp[1]:        # 찾는 코드와 같으면
      return tp[0]            # 해당하는 문자 반환
    
def make_morse_tree():
    root = BTNode(None, None, None)     
    for tp in table:                    # tp: 모스 코드 표의 각 항목
        code = tp[1]                    # tp[1]: 모스 코드
        node = root                     # 루트부터 탐색 시작
        for c in code:
            if c == '.':               # 점(.)이면 왼쪽으로 이동
                if node.left == None:  # 왼쪽 자식이 비었으면 빈 노드를 추가
                    node.left = BTNode(None, None, None)
                node = node.left       # 왼쪽 자식으로 이동
            elif c == '-':             # 선(-)이면 오른쪽으로 이동
                if node.right == None: # 오른쪽 자식이 비었으면 빈 노드를 추가
                    node.right = BTNode(None, None, None)
                node = node.right      # 오른쪽 자식으로 이동
        node.data = tp[0]              # 최종 노드에 문자(tp[0])를 저장
    return root

def decode(root, code):                 # 루트 노드에서 시작
    node = root
    for c in code:                      # 각 부호에 대해
        if c == '.':                    # 점(·): 왼쪽으로 이동
            node = node.left
        elif c == '-':                  # 선(-): 오른쪽으로 이동
            node = node.right
    return node.data                    # 문자 반환

morseCodeTree = make_morse_tree()             # 모스 코드 결정트리를 만듦
str = input("입력 문장 : ")                     
mlist = []
for ch in str:                                # 입력 문자열의 각 문자를 순서대로
    code = encode(ch)                         # 모스 코드로 변환
    mlist.append(code)                        # 리스트에 추가
print("Morse Code: ", mlist)
print("Decoding: ", end='')
for code in mlist:                            # 리스트의 모스 코드를 하나씩 꺼내서
    ch = decode(morseCodeTree, code)          # 디코딩
    print(ch, end='')                         # 결과 문자 출력
print()                                       # 줄 바꿈