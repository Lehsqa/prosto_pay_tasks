class Node:
    '''
    Implementation Choice: The Node class is used to create nodes that store a key-value pair and a reference to the
    next node.

    Argumentation: This implementation is straightforward and efficient for creating a singly linked list. It contains
    attributes for the key, value, and a reference to the next node. It allows for easy insertion and traversal of
    elements in the linked list.
    '''
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class LinkedList:
    '''
    Implementation Choice: The LinkedList class is implemented as a singly linked list where each node contains a
    key-value pair.

    Argumentation: This implementation is suitable for the purpose of a linked list. It has methods for adding,
    getting, and removing elements efficiently. When adding or updating a key-value pair, it checks if the key already
    exists and updates the value accordingly. It handles edge cases like adding to an empty list and removing
    the head node.
    '''
    def __init__(self):
        self.head = None

    def add(self, key, value) -> None:
        node = Node(key, value)
        current = self.head
        old_node = self.get(key)

        if old_node:
            old_node.value = value
            return

        if current:
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def get(self, key) -> Node:
        current = self.head

        if current:
            while current:
                if current.key == key:
                    return current
                current = current.next

    def remove(self, key) -> None:
        current = self.head
        prev = None

        try:
            if current.key == key:
                self.head = current.next
            else:
                while current:
                    if current.key == key:
                        break
                    prev = current
                    current = current.next
                if current is None:
                    return
                prev.next = current.next
                del current
        except AttributeError:
            return

    def serialize(self) -> str:
        current = self.head
        ls = []
        while current:
            ls.append([current.key, current.value])
            current = current.next
        return str(ls)


class HashMap:
    '''
    Implementation Choice: The HashMap class uses a list of linked lists (buckets) to implement a basic hash map.
    It calculates the index for each key using a custom hash function and stores key-value pairs in the
    corresponding bucket.

    Argumentation: This implementation is a simple hash map with chaining to handle collisions. Chaining is a good
    choice when the number of keys is not known in advance, as it allows for dynamic resizing. The custom hash
    function supports both integer and string keys. The code efficiently handles putting, getting, and
    removing key-value pairs by distributing them across buckets based on their hash values. The __str__ method
    serializes the entire hash map for easy visualization.
    '''
    def __init__(self, size: int):
        self.size = size
        self.buckets = [LinkedList() for _ in range(self.size)]

    def _hash(self, key) -> int:
        count = 0

        if key is None:
            raise KeyError('key can`t be None')
        elif type(key) == int:
            return key % self.size
        else:
            for i in key:
                count += ord(i)
            return count % self.size

    def put(self, key, value) -> None:
        index = self._hash(key)
        self.buckets[index].add(key, value)

    def get(self, key) -> str:
        index = self._hash(key)
        res = self.buckets[index].get(key)

        if res is not None:
            return str([res.key, res.value])

    def remove(self, key) -> None:
        index = self._hash(key)
        self.buckets[index].remove(key)

    def __str__(self):
        return ''.join(str(item.serialize()) for item in self.buckets)
