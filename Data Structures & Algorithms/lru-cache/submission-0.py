class Node:
    
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1
        node = self.hash[key]
        self.remove(node)
        self.insert(node)
        return node.val  

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])
        new_node = Node(key, value)
        self.hash[key] = new_node
        self.insert(new_node)
        if len(self.hash) > self.capacity:
            lru = self.head.next
            self.remove(lru)
            del self.hash[lru.key]