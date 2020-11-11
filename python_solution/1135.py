class Solution:
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        # Solution 1: Prim's algorithm (612ms: 87.80%)
        dic = defaultdict(dict)
        number = 0
        for u, v, c in connections:
            if v in dic[u]:
                dic[u][v] = min(c, dic[u][v])
                dic[v][u] = min(c, dic[v][u])
            else:
                dic[u][v] = c
                dic[v][u] = c
                number += 1
        if number<N-1:
            return -1
        h = []
        res = 0
        temp = N-1
        start = 1
        visited = {start:True}
        while temp>0:
            for node in dic[start]:
                heappush(h, (dic[start][node], node))
            while h and h[0][1] in visited:
                heappop(h)
            cost, newnode = heappop(h)
            res += cost
            visited[newnode] = True
            start = newnode
            temp -= 1
        return res
        
        # Solution 2: Kruscal algorithm by Union Find (608ms: 88.98%)
        parent = [i for i in range(N)]
        rank = [1 for _ in range(N)]

        def find(node):
            if parent[node]!=node:
                parent[node] = find(parent[node])
            return parent[node]
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)
            if p1==p2:
                return False
            if rank[p1]<rank[p2]:
                parent[p1] = p2
                rank[p2] += rank[p1]
            else:
                parent[p2] = p1
                rank[p1] += rank[p2]
            return True
        
        connections.sort(key = lambda x: x[2])
        res = number = 0
        for u, v, c in connections:
            if union(u-1, v-1):
                res += c
                number += 1
        return res if number==N-1 else -1