class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Solution 1: Hash + Sort (132ms: 45.26%)
        temp = Counter(nums)
        ele = [[key, temp[key]] for key in temp.keys()]
        ele = sorted(ele, key = lambda x: x[1], reverse = True)
        return [x[0] for x in ele[:k]]
        
        # Solution 2: Use Heap from Python (172ms: 20.66%)
        if k==len(nums): return nums # Avoid the O(NlogN) time
        ele = Counter(nums)
        return heapq.nlargest(k, ele.keys(), ele.get)
        
        # Solution 3: More basic operation from Heap
        dic1 = {}
        for item in nums:
            if item in dic1:
                dic1[item] += 1
            else:
                dic1[item] = 1
        h = heapq.heapify([float('Inf')])
        dic2 = {}
        for key in dic1.keys():
            temp = dic1[key]
            if temp not in dic2:
                dic2[temp] = [key]
                heapq.heappush(h, -temp)
            else:
                dic2[temp].append(key)
        res = []
        while len(res)<k:
            temp = -heapq.heappop(h)
            for key in dic2[temp]:
                res.append(key)
        return res