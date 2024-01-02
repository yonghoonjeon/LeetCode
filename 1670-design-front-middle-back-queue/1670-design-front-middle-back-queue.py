class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = []
        self.length = 0

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)
        self.length += 1

    def pushMiddle(self, val: int) -> None:
        self.queue.insert(self.length//2, val)
        self.length += 1

    def pushBack(self, val: int) -> None:
        self.queue.append(val)
        self.length += 1

    def popFront(self) -> int:
        if self.length:
            self.length -= 1
            return self.queue.pop(0)
        return -1

    def popMiddle(self) -> int:
        if self.length:
            self.length -= 1
            return self.queue.pop(self.length//2)
        return -1

    def popBack(self) -> int:
        if self.length:
            self.length -= 1
            return self.queue.pop()
        return -1


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()