class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        
        in_degree = defaultdict(int)
        out_vertex = defaultdict(list)
        for item in prerequisites:
            in_degree[item[0]] += 1
            out_vertex[item[1]].append(item[0])
        for vertex in range(numCourses):
            if in_degree[vertex] == 0:
                res.append(vertex)
        
        for item in res:
            for vertex in out_vertex[item]:
                in_degree[vertex] -= 1
                if in_degree[vertex] == 0:
                    res.append(vertex)
        return res if len(res)==numCourses else []