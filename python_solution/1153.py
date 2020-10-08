class Solution:
    def canConvert(self, str1: str, str2: str) -> bool:
        # Solution 1 by myself: Topological + XXX (32ms: 56.89%)
        # Very tedious!!! WA for 5 times...
        out_degree = defaultdict(int)
        in_degree = defaultdict(int)
        edges = {}
        all_v = set()
        used = 0
        
        for i in range(len(str1)):
            if str1[i] in edges and str2[i]!=edges[str1[i]]:
                return False
            if str1[i] not in edges:
                out_degree[str1[i]] += 1
                in_degree[str2[i]] += 1
            edges[str1[i]] = str2[i]
            all_v.add(str1[i])
            all_v.add(str2[i])
            if str1[i]==str2[i]:
                used += 1
        
        queue = deque([])
        for key in out_degree:
            if in_degree[key]==0 or edges[key]==key:
                queue.append(key)
        
        zero_degree_num = 0
        while queue:
            node = queue.popleft()
            zero_degree_num += 1
            if node in edges and edges[node]!=node:
                in_degree[edges[node]] -= 1
                if in_degree[edges[node]]==0:
                    queue.append(edges[node])
        
        #print(len(all_v))
        #print(zero_degree_num)
        
        if (zero_degree_num==0 and len(all_v)<26) or zero_degree_num>used+len(all_v)-26:
            return True
        if (zero_degree_num<len(all_v) and zero_degree_num==used):
            return False
        return True
        
        # Solution 2 from discussion: very simple!!!
        # This problem is not enough if we judge whether there is a circle in graph
        # we need to know if we still have some 'useful' points to switch.
        edges = {}
        if str1==str2: return True
        for i in range(len(str1)):
            if str1[i] in edges and edges[str1[i]]!=str2[i]:
                return False
            edges[str1[i]] = str2[i]
        return len(set(str2))<26