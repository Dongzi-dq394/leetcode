class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # Solution 1: Use Heap from Python (340ms: 17.59%)
        heap = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                heapq.heappush(heap, matrix[i][j])
        while k:
            res = heapq.heappop(heap)
            k -= 1
        return res
        
        # Solution 2: Binary Search from discussion (168ms: 98.15%)
        def cal_rank(value):
            i, j = len(matrix)-1, 0
            rank = 0
            while j<len(matrix[0]):
                while i>=0 and matrix[i][j]>value:
                    i -= 1
                if i>=0:
                    rank += (i+1)
                j += 1
            return rank
        left, right = matrix[0][0], matrix[-1][-1]
        while left<right:
            middle = (left+right) // 2
            rank = cal_rank(middle)
            if rank>=k:
                right = middle
            else:
                left = middle+1
        return left