from sys import argv
from copy import deepcopy


def main():
    cards = {}
    my_cards = []
    with open(argv[1], "r") as fp:
        _copy = 0
        for n, data in enumerate(fp.readlines()):
            winning = list(map(lambda x: int(x) if x else "", data.split(":")[-1].split("|")[0].split(" ")))
            my_numbers = list(map(lambda x: int(x) if x else "-", data.split("|")[-1].split(" ")))
            in_winnings = list(filter(lambda x: x in winning, my_numbers))
            cards[n + 1] = [1, len(in_winnings)]
    ans = 0
    for j in deepcopy(cards):
        for i in range(cards[j][0]):
            # print(f"Card [{j}]")
            ans += 1
            for m in range(cards[j][1] + 1):
                cards[j + m][0] += 1

    print(ans)


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
