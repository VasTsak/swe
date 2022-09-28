"""
Least Recently Used Cache

We have briefly discussed caching as part of a practice problem while studying hash maps.
The lookup operation (i.e., get()) and put() / set() is supposed to be fast for a cache memory.
While doing the get() operation, if the entry is found in the cache, it is known as a cache hit. 
If, however, the entry is not found, it is known as a cache miss.
When designing a cache, we also place an upper bound on the size of the cache. 
If the cache is full and we want to add a new entry to the cache, we use some criteria 
to remove an element. After removing an element, we use the put() operation to insert 
the new element. The remove operation should also be fast.
For our first problem, the goal will be to design a data structure known as a Least Recently 
Used (LRU) cache. An LRU cache is a type of cache in which we remove the least recently used 
entry when the cache memory reaches its limit. For the current problem, consider both get and 
set operations as an use operation.
Your job is to use an appropriate data structure(s) to implement the cache.
* In case of a cache hit, your get() operation should return the appropriate value.
* In case of a cache miss, your get() should return -1.
* While putting an element in the cache, your put() / set() operation must insert the element. 
If the cache is full, you must write code that removes the least recently used entry first 
and then insert the element. All operations must take O(1) time.
For the current problem, you can consider the size of cache = 5.
@author: vasileios.tsakalos
"""

class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def set_key(self, key):
        new_node = Node(key)
        if self.head is None:
            self.head = key
            self.tail = self.head
            self.size = 1
        else:
            # Assign the new node as head
            new_node.next = self.head 
            self.head = new_node
            while new_node.next:
                if key == new_node.next.key:
                    new_node.next = new_node.next.next
                    return
                new_node = new_node.next
            self.size += 1 # it increases the size only if new key is added.
    
    def get_key(self, key):

        if self.head is None:
            return None
        
        if self.head.key == key:
            return self.head.key
        
        node = self.head

        while node.next:
            if key == node.next.key:
                node.next = node.next.next
                break
            node = node.next
        
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        return self.head.key

    def delete_tail(self):

        node = self.head
        while node:
            if node.next is None:
                self.tail = node
            node = node.next
        tail = self.tail.key
        self.tail = None
        self.size -= 1
        return tail
    
class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.HashTable = dict()
        self.storage = LinkedList

    def get(self, key):
        # return key if available, otherwise -1
        if key in self.HashTable:
            return self.HashTable[self.storage.get_key(key)]
        else:
            return -1
    
    def set(self, key, value):
        # I set the value to the key first in case the key 
        # is already present in the hash table
        if key not in self.HashTable:
            self.storage.set_key(key)
        self.HashTable[key] = value
        # Set the value if the key is not present in the cache. 
        # If the cache is at capacity remove the oldest item.
        if self.storage.size > self.capacity:
            del self.HashTable[self.storage.delete_tail()]
                

our_cache = LRU_Cache(5)
