from sys import argv
from itertools import cycle, product
from string import ascii_uppercase as ls


def main2():
    ...


def main():
    dicto: dict[str, list[str]] = {}
    runs = []
    first: str = ""
    allpos = ["".join(i) for i in list(product(ls, repeat=3))]
    with open(argv[1], "r") as fp:
        _line = fp.readline().strip()
        runs = [0 if i == "L" else 1 for i in _line]
        fp.readline()
        for n, i in enumerate(fp.readlines()):
            key = i.split("=")[0].strip()
            value = [x.strip() for x in i.split("= (")[-1].split(",")]
            value[1] = value[1][:-1].strip()
            dicto[key] = value
            if not first:
                first = key
    ans = "AAA"
    count = 0
    rLen = len(runs)
    for i in cycle(runs):
        if ans == "ZZZ":
            break
        # print(ans, i)
        ans = dicto[ans][i]
        count += 1
    print(count)


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
