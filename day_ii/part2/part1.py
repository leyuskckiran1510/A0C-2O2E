import re
from functools import reduce
from sys import argv

# base only 12 red cubes, 13 green cubes, and 14 blue cubes?


def main() -> None:
    each_game = []
    with open(argv[1], "r") as fp:
        for i in fp.readlines():
            maxes = [0, 0, 0]
            for j in i.split(";"):
                for n, k in enumerate(["red", "blue", "green"]):
                    _x = re.findall(rf"(\d+)\s{k}", j)
                    if _x:
                        _x = int(_x[0].split(" ")[0])
                        maxes[n] = _x if _x > maxes[n] else maxes[n]
            each_game.append(reduce(lambda x, y: x * y, maxes))
    print(sum((each_game)))


if __name__ == "__main__":
    if len(argv) < 2:
        print("Please Provde a input file")
    else:
        main()
