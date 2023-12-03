from sys import argv


def main():
    direct = [
        [0, 1],
        [1, 0],
        [1, 1],
        [-1, 1],
        [1, -1],
        [0, -1],
        [-1, 0],
        [-1, -1],
    ]
    with open(argv[1], "r") as fp:
        array = fp.readlines()
        gears: dict = {}
        gear_loc = []
        for row, y in enumerate(array):
            trackback = 0
            found = False
            for col, x in enumerate(list(y)):
                if x.isdigit():
                    trackback = trackback * 10 + int(x)
                    for j in direct:
                        n_col = col + j[0]
                        n_row = row + j[1]
                        if (
                            n_row >= 0
                            and n_row < len(array)
                            and n_col >= 0
                            and n_col < len(array[n_row])
                            and array[n_row][n_col] == "*"
                        ):
                            gear_loc = (n_col, n_row)
                            found = True

                elif found:
                    gears[gear_loc] = gears.get(gear_loc, []) + [trackback]
                    gear_loc = ()
                    trackback = 0
                    found = False
                else:
                    trackback = 0
    sums = 0
    for i in gears:
        while gears[i]:
            _a = gears[i].pop(0)
            if gears[i]:
                sums += _a * gears[i].pop(0)

    print(gears, sums)


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
