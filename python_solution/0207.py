class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) <= 1: return True
        
        In_degree = defaultdict(int)
        Out_point = defaultdict(list)
        stack = []
        for item in prerequisites:
            Out_point[item[0]].append(item[1])
            In_degree[item[1]] += 1
        for i in range(numCourses):
            if In_degree[i] == 0:
                stack.append(i)
        
        nums = 0
        while stack:
            point = stack.pop(0)
            nums += 1
            for vertex in Out_point[point]:
                In_degree[vertex] -= 1
                if In_degree[vertex] == 0:
                    stack.append(vertex)
        return nums == numCourses