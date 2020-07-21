class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.ele = {}
        self.LRU = []

    def get(self, key: int) -> int:
        if key in self.ele:
            self.LRU.remove(key)
            self.LRU.append(key)
            return self.ele[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.ele) == self.capacity:
            if key in self.ele:
                self.LRU.remove(key)
                self.LRU.append(key)
                self.ele[key] = value
            else:
                pop_key = self.LRU.pop(0)
                self.ele.pop(pop_key)
                self.ele[key] = value
                self.LRU.append(key)
        else:
            if key in self.ele:
                self.LRU.remove(key)
                self.LRU.append(key)
                self.ele[key] = value
            else:
                self.ele[key] = value
                self.LRU.append(key)
            


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)