class DoubleList:
    def __init__(self):
        self.key = 0
        self.val = 0
        self.next = None
        self.pre = None

class LRUCache:
    # This is the total new method using double linked list. (224ms: 63.61)
    # By this, we can easily move any node to head or delete it in O(1).
    
    # Also, from discussion, this problem can be solved by OrderedDict from Python

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.num = 0
        self.dic = {}
        self.head = DoubleList()
        self.tail = DoubleList()
        self.head.next = self.tail
        self.tail.pre = self.head

    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        else:
            node = self.dic[key]
            self.DeleteNode(node)
            self.AddNode(node)
            return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic[key].val = value
            node = self.dic[key]
            self.DeleteNode(node)
            self.AddNode(node)
        else:
            newnode = DoubleList()
            newnode.key = key
            newnode.val = value
            self.dic[key] = newnode
            self.AddNode(newnode)
            self.num += 1
            if self.num>self.capacity:
                node = self.RemoveNode()
                del self.dic[node.key]
                self.num -= 1
    
    def AddNode(self, node):
        node.pre = self.head
        node.next = self.head.next
        self.head.next = node
        self.head.next.next.pre = node
    
    def DeleteNode(self, node):
        pre = node.pre
        nex = node.next
        pre.next = nex
        nex.pre = pre
        
    def RemoveNode(self):
        node = self.tail.pre
        self.DeleteNode(node)
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)