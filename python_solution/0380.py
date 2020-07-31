class RandomizedSet:
    # Solution 1: by myself (400ms)
    # Solution 2: from discussion, use dict to store the index of each element (132ms)

    def __init__(self):
        """
        Initialize your data structure here.
        """
        '''
        self.ele = {}
        self.length = 0
        '''
        self.dic = {}
        self.ele = []
        self.length = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        '''
        if val in self.ele:
            return False
        self.ele[val] = 1
        self.length += 1
        return True
        '''
        if val in self.dic:
            return False
        self.dic[val] = self.length
        self.ele.append(val)
        self.length += 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        '''
        if val in self.ele:
            self.ele.pop(val)
            self.length -= 1
            return True
        return False
        '''
        if val not in self.dic:
            return False
        index = self.dic[val]
        self.dic[self.ele[-1]] = index
        # Use swap to change the val to the last one of self.ele
        self.ele[index], self.ele[-1] = self.ele[-1], self.ele[index]
        self.ele.pop()
        self.dic.pop(val)
        self.length -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        '''
        index = random.randint(0, self.length-1)
        return list(self.ele.keys())[index]
        '''
        index = random.randint(0, self.length-1)
        return self.ele[index]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()