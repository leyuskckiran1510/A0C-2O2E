import re
from sys import argv

# base only 12 red cubes, 13 green cubes, and 14 blue cubes?


def main() -> None:
    print(
        sum(
            [
                int(re.match(r"Game\s(\d+):", i).group(1))
                for i in open(argv[1], "r").readlines()
                if all(
                    [
                        sum(map(lambda x: int(x.split(" ")[0]), re.findall(r"(\d+)\sblue", j))) <= 14
                        and sum(map(lambda x: int(x.split(" ")[0]), re.findall(r"(\d+)\sred", j))) <= 12
                        and sum(map(lambda x: int(x.split(" ")[0]), re.findall(r"(\d+)\sgreen", j))) <= 13
                        for j in i.split(";")
                    ]
                )
            ]
        )
    )


if __name__ == "__main__":
    if len(argv) < 2:
        print("Please Provde a input file")
    else:
        main()
