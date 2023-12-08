from sys import argv
from itertools import cycle, product
from string import ascii_uppercase as ls
from math import lcm


def main():
    dicto: dict[str, list[str]] = {}
    runs: list[int] = []
    items = []
    with open(argv[1], "r") as fp:
        _line = fp.readline().strip()
        runs = [0 if i == "L" else 1 for i in _line]
        fp.readline()
        for i in fp.readlines():
            key = i.split("=")[0].strip()
            value = [x.strip() for x in i.split("= (")[-1].split(",")]
            value[1] = value[1][:-1].strip()
            dicto[key] = value
            if key.endswith("A"):
                items.append(key)
    ans = ""
    count = 0
    counts = []
    for each in items:
        count = 0
        ans = each
        for i in cycle(runs):
            ans = dicto[ans][i]
            count += 1
            if ans.endswith("Z"):
                break
        counts.append(count)
    print("The Answer Is ", lcm(*counts))


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
