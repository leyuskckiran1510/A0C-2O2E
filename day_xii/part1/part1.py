import re
from sys import argv


def matches(string: str, cond: list[int]):
    return [len(i) if all([j == "#" for j in i]) else -1 for i in re.split(r"[\.]+", string=string) if i] == cond


def form_new(front: str, back: str, cond: list[int]):
    new_str = ""
    _i = cond.pop(0)
    skip = False
    for k in back:
        if skip:
            skip = False
            new_str += "."
            continue
        if k == "#" or k == "?":
            new_str += "#"
            _i -= 1
        elif k == ".":
            skip = False
            new_str += "."
            continue

        if _i == 0:
            skip = True
            if cond:
                _i = cond.pop(0)
            else:
                break

    print(cond, new_str, matches(new_str, cond=cond))
    return new_str


def solve_row(area: str, contion: str) -> int:
    carr = list(map(lambda x: int(x), contion.split(",")))
    _count = 0
    combinations = set()
    while True:
        new = form_new(area[:_count], area[_count:], carr.copy())
        if new in combinations:
            break
        if matches(new, carr):
            _count += 1
        combinations.add(new)
    return _count


def main():
    ans = 0
    with open(argv[1], "r") as fp:
        for i in fp.readlines():
            area, condtin = i.split(" ")
            ans += solve_row(area, condtin)
    print(ans)


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
