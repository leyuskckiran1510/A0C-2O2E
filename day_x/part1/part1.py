import collections
from sys import argv
from time import sleep
import time

"""
| is a vertical pipe connecting north and south.
- is a horizontal pipe connecting east and west.
L is a 90-degree bend connecting north and east.
J is a 90-degree bend connecting north and west.
7 is a 90-degree bend connecting south and west.
F is a 90-degree bend connecting south and east.
. is ground; there is no pipe in this tile.
S is the starting position of the animal; there is 
    a pipe on this tile, but your sketch doesn't show what shape the pipe has.
//mapping for better visulization
"""

pipes = {
    "|": "│",
    "-": "─",
    "L": "└",
    "J": "┘",
    "7": "┐",
    "F": "┌",
    ".": ".",
    "S": "S",
}
NON_PIPE = 0
PIPE = 1


class Node:
    def __init__(self, value, ix, iy) -> None:
        self.value = value
        self.ix = ix
        self.iy = iy
        self.parent = None
        self.depth = 1
        self.visited = False
        self.childs: list[Node] = []
        self.dirct = self.calc_direct()
        self.color = [255 * i for i in self.dirct]
        self.type = any(self.dirct)

    def calc_direct(self):
        tblr = [0, 0, 0, 0]
        if self.value == "|":
            tblr = [1, 1, 0, 0]
        elif self.value == "-":
            tblr = [0, 0, 1, 1]
        elif self.value == "L":
            tblr = [1, 0, 0, 1]
        elif self.value == "J":
            tblr = [1, 0, 1, 0]
        elif self.value == "7":
            tblr = [0, 1, 1, 0]
        elif self.value == "F":
            tblr = [0, 1, 0, 1]
        elif self.value == "S":
            tblr = [1, 1, 1, 1]

        return tblr

    def connects(self, other: "Node"):
        _cont = False
        if self.ix == other.ix:
            if self.iy < other.iy:
                _cont = self.dirct[1] & other.dirct[0]
            else:
                _cont = self.dirct[0] & other.dirct[1]
        else:
            if self.ix < other.ix:
                _cont = self.dirct[3] & other.dirct[2]
            else:
                _cont = self.dirct[2] & other.dirct[3]
        return _cont

    def __repr__(self) -> str:
        # return f"{pipes.get(self.value,self.value)}"
        return f"{self.value}{self.childs}"


directions = [
    [0, 1],
    [0, -1],
    [-1, 0],
    [1, 0],
]


def make_path(matrix: list[list[Node]], root_node: Node):
    queue = [root_node]
    max_depth = 0
    collection = [root_node]

    while queue:
        cur_node = queue.pop(0)
        if cur_node.visited:
            continue
        # time.sleep(0.1)
        # display_matrix(matrix=matrix)
        collection.append(cur_node)
        for dx, dy in directions:
            x = cur_node.ix + dx
            y = cur_node.iy + dy
            if (
                y >= 0
                and y < len(matrix)
                and x >= 0
                and x < len(matrix[y])
                and matrix[y][x].value not in ". "
                and matrix[y][x].connects(cur_node)
                and matrix[y][x].visited == False
                and matrix[y][x].parent == None
                and matrix[y][x] not in collection
            ):
                cur_node.visited = True
                matrix[y][x].parent = cur_node
                matrix[y][x].color = cur_node.color
                matrix[y][x].depth = cur_node.depth + 1
                if matrix[y][x].depth > max_depth:
                    max_depth = matrix[y][x].depth
                cur_node.childs.append(matrix[y][x])
        queue.extend(cur_node.childs)
    print(max_depth)
    return max_depth


def display_matrix(matrix: list[list[Node]]):
    print("\x1b[0J\x1b[0;0H", end="")
    for rvalue in matrix:
        for cvalue in rvalue:
            v = pipes.get(cvalue.value, cvalue)
            color = "\x1b[38;2;{};{};{};{}m".format(*cvalue.color)
            if cvalue.visited:
                print(f"{color}{v}\x1b[m", end="")
            else:
                print(f"\x1b[38;2;255;100;100m{v}\x1b[m", end="")
        print("")


def main():
    matrix: list[list[Node]] = []
    root_node: Node | None = None
    ans = 0
    with open(argv[1], "r") as fp:
        for row, i in enumerate(fp.readlines()):
            _temp = []
            for col, v in enumerate(i.strip()):
                _node = Node(v, col, row)
                if v == "S":
                    root_node = _node
                _temp.append(_node)
            matrix.append(_temp)
    if root_node:
        ans = make_path(matrix, root_node)
    # display_matrix(matrix)
    print(root_node)
    print(ans - 1)


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
