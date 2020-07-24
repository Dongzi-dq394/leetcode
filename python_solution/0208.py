class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        temp = self.trie
        for item in word:
            if item not in temp:
                temp[item] = {}
            temp = temp[item]
        temp['*'] = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        temp = self.trie
        for item in word:
            if item not in temp:
                return False
            temp = temp[item]
        return '*' in temp
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.trie
        for item in prefix:
            if item not in temp:
                return False
            temp = temp[item]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)