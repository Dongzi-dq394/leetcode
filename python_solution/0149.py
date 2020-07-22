class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # Something to learn from this problem:
        # 1. [] is not hashable but () is.
        # 2. float or double number calculation is not accurate sometime.
        # 3. we need to consider the points sharing the same position
        def slope(i, j):
            x1, x2 = points[i][0], points[j][0]
            y1, y2 = points[i][1], points[j][1]
            if x1 == x2: return (0, 0)
            if y1 == y2: return (float('Inf'), float('Inf'))
            x, y = x1 - x2, y1 - y2
            if x < 0:
                x, y = -x, -y
            temp = math.gcd(x, y)
            return (x/temp, y/temp)
        if not points: return 0
        res = 1
        for i in range(len(points)-1):
            dic = defaultdict(int)
            same_pos = 0
            for j in range(i+1, len(points)):
                if points[j][0] == points[i][0] and points[j][1] == points[i][1]:
                    same_pos += 1
                    continue
                else:
                    s = slope(i, j)
                    dic[s] += 1
            if dic.values():
                res = max(res, 1+same_pos+max(dic.values()))
            else:
                res = max(res, 1+same_pos)
        return res