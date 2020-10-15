class FileSystem:
    
    # Solution 1: Trie (292ms: 66.96%)

    def __init__(self):
        self.trie = {}

    def createPath(self, path: str, value: int) -> bool:
        ele = path[1:].split('/')
        temp = self.trie
        for i in range(len(ele)-1):
            if ele[i] not in temp:
                return False
            temp = temp[ele[i]]
        if ele[-1] not in temp:
            temp[ele[-1]] = {}
        temp = temp[ele[-1]]
        if '*' in temp:
            return False
        temp['*'] = value
        return True

    def get(self, path: str) -> int:
        ele = path[1:].split('/')
        temp = self.trie
        for i in range(len(ele)):
            if ele[i] not in temp:
                return -1
            temp = temp[ele[i]]
        return temp['*'] if '*' in temp else -1


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)