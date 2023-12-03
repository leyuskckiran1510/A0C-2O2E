import pdb
from sys import argv


def main():
    answer = 0
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
    has_sym = []
    with open(argv[1], "r") as fp:
        array = fp.readlines()
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
                            and array[n_row][n_col] not in ".\n"
                            and not array[n_row][n_col].isdigit()
                        ):
                            found = True

                elif found:
                    has_sym.append(trackback)
                    trackback = 0
                    found = False
                else:
                    trackback = 0
    print(sum(has_sym), has_sym)


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
