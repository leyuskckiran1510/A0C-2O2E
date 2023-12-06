from functools import reduce
from sys import argv


def main():
    times = []
    distances = []
    each = []
    with open(argv[1], "r") as fp:
        times = list(map(int, filter(lambda x: x, fp.readline().split(":")[-1].strip().split(" "))))
        distances = list(map(int, filter(lambda x: x, fp.readline().split(":")[-1].strip().split(" "))))
    times = [int("".join([str(i) for i in times]))]
    distances = [int("".join([str(i) for i in distances]))]
    for x, y in zip(times, distances):
        left = 1
        right = x - left
        count = 0
        while left <= x:
            if left * (x - left) > y:
                count += 1
            left += 1
            # right -= 1
        # if count % 2:
        #     count = (count - 1) * 2 + 1
        # else:
        #     count = count * 2
        each.append(count)
    print(each, reduce(lambda x, y: x * y, each))


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
