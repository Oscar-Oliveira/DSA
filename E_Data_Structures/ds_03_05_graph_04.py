"""
A* Algorithm
- See: https://www.youtube.com/watch?v=KNXfSOx4eEE
- See: https://brilliant.org/wiki/a-star-search/
"""

import heapq
import math

class PriorityQueue:

    def __init__(self):
        self.elements = []

    def is_empty(self):
        return len(self.elements) == 0

    def enqueue(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def dequeue(self):
        return heapq.heappop(self.elements)[1]

class Board():

    COST_LINE = 10
    COST_DIAGONAL = math.sqrt((COST_LINE ** 2) * 2)  # float("inf")

    @staticmethod
    def distance(point1, point2):
        """Calculate Manhattan distance"""
        (r1, c1), (r2, c2) = point1, point2
        return abs(r1 - r2) + abs(c1 - c2)

    @staticmethod
    def cost(row, column):
        value = abs(row) + abs(column)
        return value * Board.COST_LINE if value < 2 else Board.COST_DIAGONAL

    def __init__(self, size, empty_symbol, wall_symbol):
        self.__size = size
        if empty_symbol == wall_symbol:
            raise ValueError("empty_symbol and wall_symbol cannot be the same")
        self.__empty_symbol = empty_symbol
        self.__wall_symbol = wall_symbol
        self.__board = [[empty_symbol for x in range(size)] for y in range(size)]

    def get_size(self):
        return self.__size

    def is_wall(self, point):
        return self.__board[point[0]][point[1]] == self.__wall_symbol

    def is_inside(self, point):
        r, c = point
        return r >= 0 and c >= 0 and r < self.__size and c < self.__size

    def are_same_points(self, point1, point2):
        (r1, c1), (r2, c2) = point1, point2
        return r1 == r2 and c1 == c2

    def is_valid_point(self, point):
        return self.is_inside(point) and not self.is_wall(point)

    def make_walls(self, walls):
        for point in walls:
            self.mark(point, self.__wall_symbol)

    def mark(self, point, fill):
        self.__board[point[0]][point[1]] = fill

    def __str__(self):
        column_template = "{:>4}"
        return_string = "\n" + column_template.format("#")
        for i in range(self.__size):
            return_string += column_template.format(i)
        return_string += "\n"
        for i in range(self.__size):
            return_string += column_template.format(i)
            for j in range(self.__size):
                return_string += column_template.format(self.__board[i][j])
            return_string += "\n"
        return return_string

class AStar():

    def __init__(self, board):
        self.__board = board
        self.__size = board.get_size()
        self.__start_row = self.__start_column = None
        self.__end_row = self.__end_column = None

    def get_h(self, h, point1, point2):
        if not h[point1[0]][point1[1]]:
            h[point1[0]][point1[1]] = Board.distance(point1, point2)
        return h[point1[0]][point1[1]]

    def get_neighbors(self, point):
        neighbors = []
        r, c = point
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                point_temp = (r + i, c + j)
                if not self.__board.are_same_points(point, point_temp):
                    if self.__board.is_valid_point(point_temp):
                        neighbors.append(point_temp)
        return neighbors

    def search(self, start, end):

        self.__start_row, self.__start_column = start
        self.__end_row, self.__end_column = end

        h = [[None for x in range(self.__size)] for y in range(self.__size)]

        g = {}
        g[start] = 0

        parent = {}
        parent[start] = None

        # make an openlist containing only the starting node
        open_list = PriorityQueue()
        open_list.enqueue((self.__start_row, self.__start_column), 0)

        # make an empty closed list
        closed_list = []

        #while (the destination node has not been reached):
        while not open_list.is_empty():

            # consider the node with the lowest f score in the open list
            current = open_list.dequeue()

            # if (this node is our destination node) :
            if self.__board.are_same_points(end, current):
                # we are finished
                break

            # put the current node in the closed list and look at all of its neighbors
            closed_list.append(current)
            for neighbor in self.get_neighbors(current):

                if neighbor not in closed_list:

                    new_cost = g[current] + Board.cost(neighbor[0] - current[0], neighbor[1] - current[1])

                    if neighbor not in g or g[neighbor] > new_cost:
                        # replace the neighbor with the new, lower, g value
                        g[neighbor] = new_cost
                        # change the neighbor's parent to our current node
                        parent[neighbor] = current
                        # priority = g + h
                        priority = new_cost + self.get_h(h, neighbor, end)
                        # add it to the open list
                        open_list.enqueue(neighbor, priority)

        return parent

    def print(self, start, finish, path, fill):
        current = path[finish]
        while current != start:
            self.__board.mark(current, fill)
            current = path[current]

def main():

    board = Board(10, ".", "\u2588")
    board.make_walls([(3,0), (3,1), (2,0), (2, 3), (3, 2), (2,2), (4, 2), (4, 3), (5, 3), (2,4), (2,5)])

    start = (2, 1)
    finish = (5, 4)

    board.mark(start, "S")
    board.mark(finish, "F")

    astar = AStar(board)
    path = astar.search(start, finish)
    astar.print(start, finish, path, "o")

    print(board)

if __name__ == "__main__":
    main()
    print("Done!!")
