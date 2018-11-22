
__author__ = Rohit Kamal Saxena
__email__  = rohit_kamal2003@yahoo.com

class Solution(object):
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        visited = set()

        def dfs(i, j, direction_i, direction_j):
            robot.clean()
            visited.add((i, j))

            for d in range(4):
                ni = i + direction_i
                nj = j + direction_j
                if (ni, nj) not in visited and robot.move():
                    dfs(ni, nj, direction_i, direction_j)
                    robot.turnRight()
                    robot.turnRight()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnRight()
                direction_i, direction_j = -direction_j, direction_i

        dfs(0, 0, 0, 1)
