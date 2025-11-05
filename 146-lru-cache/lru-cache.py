class Node:
    def __init__(self, key, val):
        self.prev = None
        self.next = None
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.MRU = Node(0, 0) # head
        self.LRU = Node(0, 0) # tail
        self.MRU.next = self.LRU # MRU <-> LRU
        self.LRU.prev = self.MRU
        
        self.d = {} # key -> actual Node
        self.cap = capacity
        self.curSize = 0

    def remove(self, node): # just remove the node from wherever it is in the list
        p = node.prev # prev <-> node <-> next ... prev <-> next
        n = node.next
        p.next = n
        n.prev = p
    
    def addToMRU(self, node): # MRU <-> oldHead ... MRU <-> node <-> oldHead
        oldHead = self.MRU.next
        self.MRU.next = node # MRU <-> node
        node.prev = self.MRU
        node.next = oldHead # node <-> oldHead
        oldHead.prev = node


    def get(self, key: int) -> int:
        # remove the node from its current place, add it to the MRU position
        # print(key, self.d.keys())
        # print(self.d)
        if key not in self.d:
            return -1
        
        node = self.d[key]
        self.remove(node)
        self.addToMRU(node)
        return node.val


    def put(self, key: int, value: int) -> None: 
        # remove the LRU if needed
        # add the node to MRU position

        if key in self.d: # just change the val
            node = self.d[key]
            node.val = value
            self.remove(node) # move to MRU
            self.addToMRU(node)
        else:
            if self.curSize == self.cap: # need to evict one
                # print(key, value)
                # print(self.d.keys())
                # print("evicted")
                lruNode = self.LRU.prev
                self.remove(lruNode)
                del self.d[lruNode.key]
                # print(self.d.keys())
                self.curSize -= 1

            
            self.curSize += 1
            newNode = Node(key, value) # make new node
            self.addToMRU(newNode)
            self.d[key] = newNode



        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)