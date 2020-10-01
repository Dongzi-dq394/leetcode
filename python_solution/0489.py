# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # Solution from Solution: DFS and Backtracking (68ms: 94.49%)
        visited = {}
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        def dfs_backtracking(i, j, cur_dir):
            visited[(i, j)] = True
            robot.clean()
            for k in range(4):
                new_dir = (cur_dir+k)%4
                di, dj = directions[new_dir]
                new_i, new_j = i+di, j+dj
                if (new_i, new_j) not in visited and robot.move():
                    dfs_backtracking(new_i, new_j, new_dir)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()
        dfs_backtracking(0, 0, 0)