from sys import argv


def main():
    ans = 0
    with open(argv[1], "r") as fp:
        for data in fp.readlines():
            winning = list(map(lambda x: int(x) if x else "", data.split(":")[-1].split("|")[0].split(" ")))
            my_numbers = list(map(lambda x: int(x) if x else "-", data.split("|")[-1].split(" ")))
            in_winnings = list(filter(lambda x: x in winning, my_numbers))
            if in_winnings:
                ans += 1 << (len(in_winnings) - 1)
            print(in_winnings)
    print(ans)


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
