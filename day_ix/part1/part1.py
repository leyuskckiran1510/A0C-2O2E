import pdb
from sys import argv


def compute_next(line: str) -> int:
    last_value = []
    items = list(map(int, line.strip().split(" ")))
    while True:
        last_value.append(items[-1])
        _new = []
        for n, i in enumerate(items[:-1]):
            _new.append(items[n + 1] - items[n])
        items = _new.copy()
        # input()
        if all([not i for i in items]):
            break

    return sum(last_value)


def main():
    next_value: list[int] = []
    with open(argv[1], "r") as fp:
        for n, line in enumerate(fp.readlines()):
            next_value.append(compute_next(line))
    print("The Answer Is [%d]" % (sum(next_value)))


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
