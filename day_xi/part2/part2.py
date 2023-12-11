from sys import argv
from itertools import combinations

SCALE_INDEX = 1000000
# SCALE_INDEX = int(argv[2])


class Coordinate:
    def __init__(self, x: int, y: int, _id: int) -> None:
        self.x = x
        self.y = y
        self.id = _id

    def update(self, li: list[int]) -> None:
        to_add = li[: self.x].count(0)
        self.x += to_add * (SCALE_INDEX - 1)

    def distance(self, other: "Coordinate") -> int:
        """
        with pythagores theorem distance = [(x1-x2)^2+(y1-y2)^2]^(1/2)
        But as we cannot travel in diagonal direction we jut to normal
        calculation:- |x1-x2| + |y1-y2|
        """
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __repr__(self) -> str:
        return f"{self.x,self.y}[{self.id}]"


def main():
    ans = 0
    galaxies: list[Coordinate] = []
    columns = []
    missed = 0
    count = 0
    with open(argv[1], "r") as fp:
        for row, i in enumerate(fp.readlines()):
            if not columns:
                columns = [0] * len(i)
            found = False
            for col, j in enumerate(i):
                if j == "#":
                    found = True
                    columns[col] = 1
                    count += 1
                    _cord = Coordinate(col, row + (missed), count)
                    galaxies.append(_cord)
            if not found:
                missed += 1 * (SCALE_INDEX - 1)

    [i.update(columns) for i in galaxies]
    for A, B in combinations(galaxies, r=2):
        ans += A.distance(B)
        # print(A.distance(B))
    print(ans, ans == 1030)


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
