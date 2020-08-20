class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Old Solution: Topological Sort (116ms: 55.92%)
        res = []
        edges = defaultdict(list)
        degree = [0]*numCourses # This is better than dict
        for item in prerequisites:
            edges[item[1]].append(item[0])
            degree[item[0]] += 1
        queue = []
        count = 0
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        while queue:
            node = queue.pop(0)
            res.append(node)
            count += 1
            for vertice in edges[node]:
                degree[vertice] -= 1
                if degree[vertice] == 0:
                    queue.append(vertice)
        return res if count==numCourses else []
        
        # New Solution: from Solution
        # We can still use DFS
        def dfs(i, visited, edges):
            if visited[i] == 1:
                return False
            if visited[i] == 2:
                return True
            visited[i] = 1
            for vertice in edges[i]:
                if not dfs(vertice, visited, edges):
                    return False
            visited[i] = 2
            # We put the deepest node at first and then reverse
            res.append(i)
            return True
        res = []
        edges = defaultdict(list)
        visited = [0]*numCourses
        for item in prerequisites:
            edges[item[1]].append(item[0])
        for i in range(numCourses):
            if not dfs(i, visited, edges):
                return []
        return res[::-1] # Reverse is important!