class Node:
    def __init__(self, key, value, side, next=None, prev=None):
        self.key = key
        self.value = value
        self.side = side
        self.next = next
        self.prev = prev
    

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(-1, -1, 'left')
        self.right = Node(-1, -1, 'right')
        self.left.next, self.right.prev = self.right, self.left

    def removeNode(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next, next_node.prev = next_node, prev_node
    
    def insertNode(self, node):
        tail = self.right
        prev = tail.prev
        node.next, node.prev = self.right, self.right.prev
        tail.prev = node
        prev.next = node

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.removeNode(node)
            self.insertNode(node)
            return self.cache[key].value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            del self.cache[key]
            self.removeNode(node)

        if len(self.cache) >= self.capacity:
            head = self.left.next
            self.removeNode(head)
            del self.cache[head.key]

        node = Node(key, value, 'middle')
        self.insertNode(node)
        self.cache[key] = self.right.prev
        
