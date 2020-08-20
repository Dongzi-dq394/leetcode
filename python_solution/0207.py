class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Solution 1: Topological Sort
        degree = defaultdict(int)
        edges = defaultdict(list)
        queue = []
        for item in prerequisites:
            degree[item[0]] += 1
            edges[item[1]].append(item[0])
        for i in range(numCourses):
            if degree[i] == 0:
                queue.append(i)
        res = 0
        while queue:
            res += 1
            node = queue.pop(0)
            for item in edges[node]:
                degree[item] -= 1
                if degree[item] == 0:
                    queue.append(item)
        return res==numCourses
        
        # New Solution 2: DFS (100ms: 87.14%)
        # Much faster than the previous one, but use more space cuz recursion
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
            return True
        visited = [0]*numCourses
        edges = defaultdict(list)
        for item in prerequisites:
            edges[item[1]].append(item[0])
        for i in range(numCourses):
            if not dfs(i, visited, edges):
                return False
        return True