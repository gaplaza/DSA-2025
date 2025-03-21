from ArrayQueue import ArrayQueue

class CircularDeque(ArrayQueue):
  def __init__(self, capacity = 10):
    super().__init__(capacity)
  
  def addRear(self, item):
    self.enqueue(item)
  def deleteFront(self):
    return self.dequeue()
  def getFront(self):
    return self.peek()
  
  def addFront(self, item):
    if not self.isFull():
      self.array[self.front] = item
      self.front = (self.front - 1 + self.capacity) % self.capacity
    else: pass
    
  def deleteRear(self):
    if not self.isEmpty():
      item = self.array[self.rear]
      self.rear = (self.rear - 1 + self.capacity) % self.capacity
      return item
    else: pass
    
  def getRear(self):
    if not self.isEmpty():
      return self.array[self.rear]
    else: pass