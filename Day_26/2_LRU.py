# Node class for doubly linked List
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key ==> node

        # Dummy Head and Tail
        self.left = Node(0, 0)   # LRU side
        self.right = Node(0, 0)  # MRU side

        self.left.next = self.right
        self.right.prev = self.left

    # Remove a node from the linked list
    def remove(self, node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

    # Insert a node before Tail 
    def insert(self, node):
        prev = self.right.prev

        node.prev = prev
        node.next = self.right

        prev.next = node
        self.right.prev = node

    # return value if key exists and move it to MRU
    def get(self, key):

        if key not in self.cache:
            return -1

        node = self.cache[key]

        # Move to MRU position
        self.remove(node)
        self.insert(node)

        return node.value

    # Insert or update key
    def put(self, key, value):

        # If key already exists, remove old node
        if key in self.cache:
            self.remove(self.cache[key])

        # Create new node
        node = Node(key, value)

        # Insert into linked list
        self.insert(node)

        # Update dictionary
        self.cache[key] = node

        # If capacity exceeded, remove LRU
        if len(self.cache) > self.capacity:

            # LRU node is next to Head
            lru = self.left.next

            self.remove(lru)

            del self.cache[lru.key]

cache = LRUCache(2)

cache.put(1, 1)
cache.put(2, 2)

print(cache.get(1))      
print(cache.get(2))     
cache.put(4, 4)          
print(cache.get(1))      
print(cache.get(3))      
print(cache.get(4))      