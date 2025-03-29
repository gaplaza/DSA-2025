from CircularDeque import CircularDeque

dq = CircularDeque()

for i in range(9):
  if i%2 == 0:
    dq.addRear(i)
  else:
    dq.addFront(i)
dq.display("홀수는 전단 짝수는 후단 삽입")

for i in range(2):
  dq.deleteFront()
for i in range(3):
  dq.deleteRear()
dq.display("전단 삭제 2번, 후단 삭제 3번")

for i in range(9, 14):
  dq.addFront(i)
dq.display("전단에 9~13 삽입")