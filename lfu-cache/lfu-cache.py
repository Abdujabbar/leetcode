from collections import defaultdict


class Node:
    def __init__(self, key, value, freq):
        self.key = key
        self.value = value
        self.freq = freq
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = Node(-1, -1, 1)
        self.tail = Node(-1, -1, 1)
        self.size = 0
        self.head.next, self.tail.prev = self.tail, self.head
        
    def append(self, node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        self.size += 1

    def print(self):
        crawl = self.head

        while crawl:
            print("key: {}, value: {}, freq: {} -> ", crawl.key, crawl.value, crawl.freq)
            crawl = crawl.next

    def delete(self, node):
        node_prev, node_next = node.prev, node.next
        node_prev.next, node_next.prev = node_next, node_prev
        self.size -= 1


class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.freq_cache = defaultdict(LinkedList)
        self.min_freq = 0

    def get(self, key):
        if key not in self.cache or self.capacity == 0:
            return -1
        if self.capacity > 1:
            node = self.cache[key]
            self.cache[key] = Node(node.key, node.value, node.freq)
            self.freq_cache[node.freq].delete(node)

            if self.freq_cache[self.cache[key].freq].size == 0:
                del self.freq_cache[self.cache[key].freq]
                if self.min_freq == self.cache[key].freq:
                    self.min_freq += 1

            self.cache[key].freq += 1
            self.freq_cache[self.cache[key].freq].append(self.cache[key])
        return self.cache[key].value

    def put(self, key, value):
        if self.get(key) != -1:
            self.cache[key].value = value
            return

        if len(self.cache) == self.capacity:
            
            head = self.freq_cache[self.min_freq].head.next
            # print("min_freq: {}, min_key: {}".format(self.min_freq, head.value))
            if head.key in self.cache:
                del self.cache[head.key]
                self.freq_cache[self.min_freq].delete(head)
                if self.freq_cache[self.min_freq].size == 0:
                    del self.freq_cache[self.min_freq]

        self.min_freq = 1
        self.cache[key] = Node(key, value, self.min_freq)
        self.freq_cache[self.min_freq].append(self.cache[key])

