def sequential_search(A, key, low, high):
  for i in range(low, high+1):
    if A[i] == key:
      return i
    return -1
    
def sequential_search_transpose(A, key, low, high):
  for i in range(low, high+1):
    if A[i] == key:
      if i > low:         # 맨 처음 요소가 아니면
        A[i], A[i-1] = A[i-1], A[i]   # 교환하기
        i = i-1           # 한 칸 앞으로 왔음
      return i            # 탐색에 성공하면 키값의 인덱스 반환
    return -1             # 탐색에 실패하면 -1 반환
  
def binary_search(A, key, low, high):
  if (low <= high):             # low가 high보다 작거나 큰 동안만 탐색 계속
    middle = (low + high) // 2
    if key == A[middle]:        # 바로 탐색 -> 중앙 레코드 인덱스 반환
      return middle
    elif (key < A[middle]):     # 왼쪽 부분리스트 탐색 -> 순환호출
      return binary_search(A, key, low, middle-1)       
    else:                       # 오른쪽 부분리스트 탐색 -> 순환호출
      return binary_search(A, key, middle+1, high)
  return -1                     # 범위를 좁히다 못해 교차했을 때 -1 반환하고 끝

def binary_search_iter(A, key, low, high):
  while (low <= high):
    middle = (low + high) //2
    if key == A[middle]:
      return middle
    elif (key > A[middle]):
      low = middle + 1          # 왼쪽 절반 버림
    else:
      high = middle - 1         # 오른쪽 절반 버림
  return -1