class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # Solution 1 by myself: from hint (556ms: 21.73%)
        people.sort()
        dic = {}
        temp = 0
        for i in range(len(people)):
            index = people[i][1]
            if i>0 and people[i][0]==people[i-1][0]:
                temp += 1
                index -= temp
            else:
                temp = 0
            start = 0
            while index>=0:
                if start not in dic:
                    index -= 1
                start += 1
            dic[start-1] = people[i]
        for key in dic.keys():
            people[key] = dic[key]
        return people
        
        # Solution 2 from discussion: Greedy (112ms: 62.79%)
        # very tricky!!!
        people.sort(key = lambda x: (-x[0], x[1]))
        res = []
        for item in people:
            res.insert(item[1], item)
        return res