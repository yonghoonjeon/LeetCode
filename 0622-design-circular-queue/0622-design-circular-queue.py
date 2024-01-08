class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

    def enQueue(self, value: int) -> bool:
        if ((self.tail + 1) % self.k == self.head):
            print("The circular queue is full\n")
            return False

        elif (self.head == -1):
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = value
            return True
        
        else:
            self.tail = (self.tail + 1) % self.k
            self.queue[self.tail] = value
            return True
        
    def deQueue(self) -> bool:
        if (self.head == -1):
            print("The circular queue is empty\n")
            return False

        elif (self.head == self.tail):
            temp = self.queue[self.head]
            self.head = -1
            self.tail = -1
            return True
        else:
            temp = self.queue[self.head]
            self.head = (self.head + 1) % self.k
            return True

    def Front(self) -> int:
        if self.head == -1:
            return -1
        else:
            return self.queue[self.head]
        
    def Rear(self) -> int:
        if self.head == -1:
            return -1
        else:
            return self.queue[self.tail]

    def isEmpty(self) -> bool:
        if self.head == -1:
            return True
        else:
            return False
        
    def isFull(self) -> bool:
        if ((self.tail + 1) % self.k == self.head):
            return True
        else:
            return False

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()