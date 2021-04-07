
class FrontMiddleBackQueue:

    def __init__(self):
        self.queue = deque([])

    def pushFront(self, val: int) -> None:
        self.queue.insert(0, val)

    def pushMiddle(self, val: int) -> None:
        self.queue.insert(len(self.queue) // 2, val)

    def pushBack(self, val: int) -> None:
        self.queue.append(val)

    def popFront(self) -> int:
        if self.queue:
            return self.queue.popleft()

        return -1

    def popMiddle(self) -> int:
        middle = len(self.queue) // 2
        if len(self.queue) % 2 == 0:
            middle -= 1
        if self.queue:
            ans = self.queue[middle]
            del self.queue[middle]
            return ans

        return -1

    def popBack(self) -> int:
        if self.queue:
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