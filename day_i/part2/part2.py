from sys import argv

valids: dict[str, int] = {
    "0": 0,
    "1": 1,
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}
MIN, MAX = 3, 5

first, last = 0, 0


def parse_line(line: str) -> tuple[int, int]:
    v1, v2 = -1, -1
    p1, p2 = 0, MIN
    poss = "zotfsen"
    length = len(line)
    while p1 < length:
        if line[p1] >= "0" and line[p1] <= "9":
            if v1 == -1:
                v1 = valids[line[p1]]
            else:
                v2 = valids[line[p1]]
        elif line[p1] in poss and (length - p1) >= MIN:
            till = MAX if length >= MAX else length
            while p2 <= till:
                if v1 == -1:
                    v1 = valids.get(line[p1 : p1 + p2], -1)
                else:
                    v2 = valids.get(line[p1 : p1 + p2], v2)
                p2 += 1
            p2 = MIN
        p1 += 1
    return v1, v2 if v2 != -1 else v1


def main() -> int:
    answer: int = 0
    with open(argv[1], "r") as fp:
        for line in fp.readlines():
            first, last = parse_line(line)
            answer += first * 10 + last
    return answer


if __name__ == "__main__":
    if len(argv) < 2:
        print("Please Provide a input file")
    else:
        _ans = main()
        print("The answer is ", _ans, _ans == 54208)
