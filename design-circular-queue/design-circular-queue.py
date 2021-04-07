class Node:
    def __init__(self, value, next, prev):
        self.value = value
        self.next = next
        self.prev = prev


class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        head, tail = Node(-1, None, None), Node(-1, None, None)
        head.next, tail.prev = tail, head
        tail.next = head
        self.head, self.tail = head, tail

    def enQueue(self, value: int) -> bool:
        if self.capacity == self.size:
            return False

        tail = self.tail
        prev = tail.prev
        node = Node(value, None, None)
        node.prev, node.next = prev, tail
        tail.prev = node
        prev.next = node
        self.size += 1
        return True

    def deQueue(self) -> bool:
        if self.size == 0:
            return False

        head = self.head.next
        prev_node, next_node = head.prev, head.next
        prev_node.next, next_node.prev = next_node, prev_node
        self.size -= 1
        return True

    def Front(self) -> int:
        head = self.head.next
        return head.value

    def Rear(self) -> int:
        tail = self.tail.prev
        return tail.value

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.capacity
