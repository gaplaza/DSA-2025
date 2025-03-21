import queue
import random

q = queue.Queue(8)

print("삽입 순서: ", end='')
while not q.full():
    v = random.randint(0, 100)
    q.put(v)
    print(v, end=' ')
print()

print("삭제 순서: ", end='')
while not q.empty():
    print(q.get(), end=' ')
print()