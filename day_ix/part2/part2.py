from sys import argv

"""
x  10  13  16  21  30  45
  m   3   3   5   9  15
    n   0   2   4   6
      o   2   2   2
        0   0   0

2-o  = 0
0-n  = o
3-m  = n
10-x = m

x = 10 - m
    10 - (3 - n)
    10 - (3 - (0 - o))
    10 - (3 - (0 - (2 - 0)))

so,
my_array = [10,3,0,2,0] # each first items of each step

ans = my_array[0] - (my_array[1] - (my_array[2] - (my_array[3] - (my_array[4] - ... my_array[n])))))

"""


def do_sub(lis):
    if not lis:
        return 0
    return lis[0] - do_sub(lis[1:])


def compute_next(line: str) -> int:
    first_values = []
    items = list(map(int, line.strip().split(" ")))
    tabs = " "
    while True:
        first_values.append(items[0])
        _new = []
        for n, _ in enumerate(items[:-1]):
            _new.append(items[n + 1] - items[n])
        items = _new.copy()
        tabs += tabs
        if all([not i for i in items]):
            break
    return do_sub(first_values)


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
