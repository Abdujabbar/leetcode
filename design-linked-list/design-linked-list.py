class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class MyLinkedList:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        head = Node(-1)
        tail = Node(-1)
        head.next, tail.prev = tail, head
        self.head, self.tail = head, tail

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        crawl = self.head.next
        while index:
            crawl = crawl.next
            index -= 1
        if crawl:
            return crawl.value

        return -1

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        head = self.head.next
        node = Node(val)
        node.prev = self.head
        node.next, head.prev = head, node
        self.head.next = node

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        node = Node(val)
        tail = self.tail
        prev = self.tail.prev
        node.next, node.prev = tail, prev
        prev.next, tail.prev = node, node

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        crawl = self.head.next

        while index:
            crawl = crawl.next
            index -= 1

        node = Node(val)
        next_node, prev_node = crawl, crawl.prev
        node.next, node.prev = next_node, prev_node
        next_node.prev, prev_node.next = node, node


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        crawl = self.head.next
        while index:
            crawl = crawl.next
            index -= 1
        
        prev_node, next_node = crawl.prev, crawl.next
        
        if prev_node and next_node:
            prev_node.next, next_node.prev = next_node, prev_node


    def print(self):
        head = self.head.next

        while head.next:
            print("value: {}".format(head.value))
            head = head.next


