class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Solution 1 by myself: Recursion (TLE!!)
        '''
        memo = {}
        def helper(cur_ring, index, length):
            if index==len(key):
                return 0
            char = key[index]
            res = float('Inf')
            for i in range(length):
                if cur_ring[i]==char:
                    temp = min(i,length-i)+1
                    new_string = cur_ring[i:]+cur_ring[:i]
                    res = min(res, temp+helper(new_string, index+1, length))
            return res
        return helper(ring, 0, len(ring))
        '''
        # Solution 2 from discussion: DP (128ms: 83.57%)
        index = defaultdict(list)
        for i, char in enumerate(ring):
            index[char].append(i)
        length = len(ring)
        dp = [0 for _ in range(length)]
        for pos in index[key[0]]:
            dp[pos] = min(pos, length-pos)+1
        for i in range(1, len(key)):
            for pos in index[key[i]]:
                temp = float('Inf')
                for j in index[key[i-1]]:
                    temp = min(temp, dp[j]+min(abs(pos-j), length-abs(pos-j)))
                dp[pos] = temp + 1
        res = float('Inf')
        for pos in index[key[-1]]:
            res = min(res, dp[pos])
        return res
        
        # Solution 3 from discussion and the first solution: Memoization (420ms: 20.66%)
        # At first, I think I can't use memoization on this problem because we keep adding
        # the index until it reaches the len(key). While, the truth is at each char of the 
        # key, we keep moving forward any time when char is in ring. So, when we backtracking
        # (go back) and choose another way, there might be some repeating sub-problem.
        memo = {}
        def helper(cur_ring, index):
            if (cur_ring, index) in memo:
                return memo[(cur_ring, index)]
            if index==len(key):
                return 0
            char = key[index]
            res = float('Inf')
            for i in range(len(cur_ring)):
                if cur_ring[i]==char:
                    steps = min(i, len(cur_ring)-i) + 1
                    res = min(res, steps+helper(cur_ring[i:]+cur_ring[:i], index+1))
            memo[(cur_ring, index)] = res
            return res
        return helper(ring, 0)