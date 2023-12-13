from sre_constants import CATEGORY_UNI_LINEBREAK
from sys import argv
from math import ceil


def even_cols(block: list[str]) -> tuple[int, bool]:
    return len(block[0]) // 2, all(map(lambda x: x[: len(x) // 2] == x[len(x) // 2 :][::-1], block))


def col_palindrom(block: list[str]) -> tuple[int, bool]:
    if not len(block[0]) % 2:
        return even_cols(block=block)
    else:
        col, found = even_cols([i[1:] for i in block])
        if found:
            return col + 1, found
        else:
            col, found = even_cols([i[0:-1] for i in block])
            return col + 1, found


def transform(block: list[str]) -> list[str]:
    _new = [""] * len(block[0])
    col = 0
    while block:
        row = block.pop()
        for n, i in enumerate(row):
            _new[n] += i
        col += 1
    return _new


def row_palindrom(block: list[str]) -> tuple[int, bool]:
    _block = transform(block.copy())
    return col_palindrom(block=_block)


def main():
    ans = 0
    contents = []
    with open(argv[1], "r") as fp:
        _temp = []
        for i in fp.readlines():
            if len(i) < 2:
                contents.append(_temp)
                _temp = []
            else:
                _temp.append(i.strip())
        if _temp:
            contents.append(_temp)
    not_founds = 0
    for block in contents:
        col, found = col_palindrom(block)
        if found:
            ans += col
        else:
            row, found = row_palindrom(block)
            if found:
                ans += 100 * row
            else:
                not_founds += 1
                # print("\n".join(block))
                # print("Colud not find mirri in this")
                # input()
    print(f"The Answer IS {ans}", f"This many blocks were not computed {not_founds}")


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
