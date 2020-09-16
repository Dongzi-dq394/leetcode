class FileSystem:

    def __init__(self):
        self.FileSystem = {}

    def ls(self, path: str) -> List[str]:
        temp = self.FileSystem
        res = []
        sub_path = path[1:].split('/')
        #print(sub_path)
        #print(temp)
        for item in sub_path:
            if item:
                temp = temp[item]
        #print(temp)
        if '*' in temp:
            return [sub_path[-1]]
        else:
            for key in temp:
                res.append(key)
            return sorted(res)

    def mkdir(self, path: str) -> None:
        temp = self.FileSystem
        sub_path = path[1:].split('/')
        for item in sub_path:
            if item:
                if item not in temp:
                    temp[item] = {}
                temp = temp[item]

    def addContentToFile(self, filePath: str, content: str) -> None:
        temp = self.FileSystem
        flag = True
        sub_path = filePath[1:].split('/')
        for item in sub_path[:-1]:
            if item:
                if item not in temp:
                    flag = False
                    temp[item] = {}
                temp = temp[item]
        if not flag or sub_path[-1] not in temp:
            temp[sub_path[-1]] = {'*':content}
        else:
            temp[sub_path[-1]]['*'] += content

    def readContentFromFile(self, filePath: str) -> str:
        temp = self.FileSystem
        sub_path = filePath[1:].split('/')
        for item in sub_path:
            if item:
                temp = temp[item]
        return temp['*']


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)