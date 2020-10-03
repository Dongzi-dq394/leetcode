class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # Solution by Hint: Hash Table (40ms: 54.46%)
        def length(ch1, ch2):
            return ord(ch2)-ord(ch1) if ch2>=ch1 else 26-ord(ch1)+ord(ch2)
        dic = defaultdict(list)
        for string in strings:
            if len(string)==1:
                dic['single'].append(string)
            else:
                key = ''
                for i in range(1, len(string)):
                    key += str(length(string[i-1], string[i]))
                    key += '#'
                dic[key].append(string)
        return list(dic.values())