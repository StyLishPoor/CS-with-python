from enum import Enum
from typing import List, NamedTuple, Callable, Optional
import random
from math import sqrt
from generic_search import dfs, node_to_path, Node

class Cell(str, Enum):
    EMPTY = " "
    BLOCKED = "X"
    START = "S"
    GOAL = "G"
    PATH = "*"

class Mazelocation(NamedTuple):
    row: int
    column: int

class Maze:
    def __init__(self, rows: int = 10, columns: int = 10, sparsness: float = 0.2, start:
        Mazelocation = Mazelocation(0,0), goal: Mazelocation = Mazelocation(9,9)) -> None:
        self.rows: int = rows
        self.columns: int = columns
        self.start: Mazelocation = start
        self.goal: Mazelocation = goal
        #空セルの設定
        self._grid: List[List[Cell]] = [[Cell.EMPTY for c in range(columns)] for r in range(rows)]
        #障害物の設定
        self._randomly_fill(rows, columns, sparsness)
        #start goal
        self._grid[start.row][start.column] = Cell.START
        self._grid[goal.row][goal.column] = Cell.GOAL
        
    
    def _randomly_fill(self, rows: int, columns: int, sparsness: float) -> None:
        for row in range(rows):
            for column in range(columns):
                if random.uniform(0,1.0) < sparsness:
                    self._grid[row][column] = Cell.BLOCKED
    
    def __str__(self) -> str:
        output: str = ""
        for row in self._grid:
            output += "".join([c for c in row]) + '\n'
        return output

    def goal_test(self,ml: Mazelocation) -> bool:
        return ml == self.goal
    
    def successors(self, ml: Mazelocation) -> List[Mazelocation]:
        locations: List[Mazelocation] = []
        if (ml.row + 1 < self.rows) and (self._grid[ml.row+1][ml.column] != Cell.BLOCKED): #枠内 and BLOCKじゃない
            locations.append(Mazelocation(ml.row + 1, ml.column))
        elif (ml.row - 1 >= 0) and (self._grid[ml.row - 1][ml.column] != Cell.BLOCKED):
            locations.append(Mazelocation(ml.row - 1, ml.column))
        elif (ml.column + 1 < self.columns) and (self._grid[ml.row][ml.column + 1] != Cell.BLOCKED):
            locations.append(Mazelocation(ml.row, ml.column + 1))
        elif (ml.column - 1 >= 0) and (self._grid[ml.row][ml.column - 1] != Cell.BLOCKED):
            locations.append(Mazelocation(ml.row, ml.column - 1))
        return locations

    def mark(self, path: List[Mazelocation]) -> None:
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.PATH
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL
    
    def clear(self, path: List[Mazelocation]) -> None:
        for maze_location in path:
            self._grid[maze_location.row][maze_location.column] = Cell.EMPTY
        self._grid[self.start.row][self.start.column] = Cell.START
        self._grid[self.goal.row][self.goal.column] = Cell.GOAL

if __name__ == "__main__":
    maze: Maze = Maze()
    print(maze)
    solution1: Optional[Node[Mazelocation]] = dfs(maze.start, maze.goal_test, maze.successors)
    if solution1 is None:
        print('No Solutions found using depth-first search!')
    else:
        path1: List[Mazelocation] = node_to_path(solution1)
        maze.mark(path1)
        print(maze)
        maze.clear(path1)




