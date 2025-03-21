from ArrayQueue import ArrayQueue

import random

q = ArrayQueue(8)

q.display("초기 상태")
while not q.isFull():
  q.enqueue(random.randint(0, 100))
q.display("포화 상태")

print("삭제 순서: ", end=' ')
while not q.isEmpty():
  print(q.dequeue(), end=' ')
print()
