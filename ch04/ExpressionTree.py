from BinaryTree import BTNode, preorder, inorder, postorder

def buildETree(expr):                              # 후위표기 수식을 expr로 전달
    if len(expr) == 0:                             # 리스트가 비어 있으면
        return None

    token = expr.pop()                             # 후위표기는 뒤에서 앞으로 처리하므로 맨 뒤 pop
    if token in "+-*/":                            # 연산자일 경우
        node = BTNode(token)                       # 노드 생성
        node.right = buildETree(expr)              # 오른쪽 서브트리 먼저 생성
        node.left = buildETree(expr)               # 왼쪽 서브트리 생성
        return node                                # 완성된 노드 반환
    else:                                          # 피연산자일 경우 (숫자)
        return BTNode(float(token))                # 단말 노드로 만들어 반환

def evaluate(node):                       # 수식 트리 계산 함수
    if node is None:                      # 공백 트리이면 0 반환
        return 0
    elif node.isLeaf():                   # 단말 노드이면 -> 피연산자
        return node.data                  # 그 노드의 값(데이터) 반환
    else:                                 # 루트나 가지 노드라면 -> 연산자
        op1 = evaluate(node.left)         # 왼쪽 서브트리 먼저 계산
        op2 = evaluate(node.right)        # 오른쪽 서브트리 계산
        if node.data == '+':              # 루트(현재 노드)를 처리
            return op1 + op2              # → 후위순회
        elif node.data == '-':
            return op1 - op2
        elif node.data == '*':
            return op1 * op2
        elif node.data == '/':
            return op1 / op2

str = input("입력(후위표기): ")                  # 후위표기식 입력
expr = str.split()                              # 토큰 리스트로 변환
print("토큰분리(expr): ", expr)
root = buildETree(expr)                         # 후위표기식을 수식 트리로 만들고 루트를 반환
print("\n전위순회: ", end=''); preorder(root)   # 전위순회 출력
print("\n중위순회: ", end=''); inorder(root)    # 중위순회 출력
print("\n후위순회: ", end=''); postorder(root)  # 후위순회 출력
print("\n계산 결과: ", evaluate(root))          # 수식 트리 계산 결과 출력