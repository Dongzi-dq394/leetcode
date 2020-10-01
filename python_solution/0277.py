# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        # Solution 1 by myself: The normal array (2512ms: 14.24%)
        candidates = {i:True for i in range(n)}
        for i in range(n):
            for j in range(n):
                if i!=j:
                    if knows(i, j):
                        candidates[i] = False
                        break
        print(candidates)
        for key in candidates:
            if candidates[key]:
                flag = True
                for i in range(n):
                    if i!=key:
                        if not knows(i, key):
                            flag = False
                            break
                if flag:
                    return key
        return -1
        
        # Solution 2 from Solution: one-pass trick (1768ms: 73.99%)
        # The key idea is: whenever the knows() is called, there will
        # be a node excluded.
        cand = 0
        for i in range(1, n):
            if knows(cand, i):
                cand = i
        for i in range(n):
            if i!=cand:
                # It's important to include the knows(cand, i)
                # here, because there might be the connection 
                # between cand and the nodes before cand.
                if not knows(i, cand) or knows(cand, i):
                    return -1
        return cand