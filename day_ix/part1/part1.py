from sys import argv

"""
10  13  16  21  30  45 x
  3   3   5   9  15  y
    0   2   4   6  z
      2   2   2  a
        0   0   0


a-2  = 0
z-6  = a
y-15 = z
x-45 = y

x = 45 + y
    45 + (15 + z)
    45 + (15 + (6 + a))
    45 + (15 + (6 + (2 + 0)))

so,
my_array = [10,3,0,2,0] # each first items of each step

ans = my_array[0] + (my_array[1] + (my_array[2] + (my_array[3] + (my_array[4] + ( ... my_array[n])))))
    = my_array[0] +  my_array[1] +  my_array[2] +  my_array[3] +  my_array[4] +   ... my_array[n])))))

"""


def compute_next(line: str) -> int:
    last_value = []
    items = list(map(int, line.strip().split(" ")))
    while True:
        last_value.append(items[-1])
        _new = []
        for n, _ in enumerate(items[:-1]):
            _new.append(items[n + 1] - items[n])
        items = _new.copy()
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
