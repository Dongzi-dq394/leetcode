class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList: return 0
        length = len(beginWord)
        dic = defaultdict(list)
        for item in wordList:
            for i in range(length):
                dic[item[:i]+'*'+item[i+1:]].append(item)
        stack = [[beginWord, 1]]
        visited = {beginWord: True}
        while stack:
            [cur_word, res] = stack.pop(0)
            for i in range(length):
                temp = cur_word[:i] + '*' + cur_word[i+1:]
                for item in dic[temp]:
                    if item == endWord:
                        return res+1
                    if item not in visited:
                        stack.append([item, res+1])
                        visited[item] = True
        return 0