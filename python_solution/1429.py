class FirstUnique:
    
    # Solution 1 by myself: Hash Table --> take use of 'pop' from hash table (720ms: 96.88%)
    # Solution 2 from Solution: Queue and Hash Table (788ms: 81.11%)

    def __init__(self, nums: List[int]):
        '''
        count = Counter(nums)
        self.unique = {}
        self.other = {}
        for item in nums:
            if count[item]==1:
                self.unique[item] = True
            else:
                if item not in self.other:
                    self.other[item] = True
        '''
        self.queue = deque([])
        count = Counter(nums)
        self.judge = {}
        for num in nums:
            self.queue.append(num)
            if count[num]==1:
                self.judge[num] = True
            else:
                self.judge[num] = False

    def showFirstUnique(self) -> int:
        '''
        if not self.unique: return -1
        for item in self.unique:
            return item
        '''
        while self.queue and not self.judge[self.queue[0]]:
            self.queue.popleft()
        if self.queue:
            return self.queue[0]
        return -1

    def add(self, value: int) -> None:
        '''
        if value not in self.other and value not in self.unique:
            self.unique[value] = True
            return
        if value in self.unique:
            self.unique.pop(value)
            self.other[value] = True
        '''
        if value not in self.judge:
            self.judge[value] = True
        else:
            self.judge[value] = False
        self.queue.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)