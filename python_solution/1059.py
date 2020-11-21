class Solution:
    def leadsToDestination(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Solution 1: DFS (296ms: 25.00%)
        record = defaultdict(list)
        for o, s in edges:
            record[o].append(s)
        visited = {i:0 for i in range(n)}
        reach = True
        def dfs(node):
            if visited[node]==1: return False
            if visited[node]==2: return True
            # if node==destination: reach=True
            visited[node] = 1
            nonlocal reach
            if len(record[node])==0:
                if node!=destination:
                    reach = False
            for nei in record[node]:
                if not dfs(nei):
                    return False
            visited[node] = 2
            return True
        non_cycle = dfs(source)
        return non_cycle and reach