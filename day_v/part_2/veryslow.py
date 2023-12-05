from sys import argv

"""
NOTE:-
Input:-
    seed-to-soil map:
    50 98 2

Expands To:-
       soil            seed
        50              98      2
    destination       source  range 
    ->50,51           98,99

Meaning:-
    soli[50] needs seed[98]
    soli[51] needs seed[99]
"""


class MagicDic:
    def __init__(self, frm: int, to: int, rng: int) -> None:
        self.frm: int = frm
        self.to: int = to
        self.rng: int = rng

    def __getitem__(self, __key: int) -> None | int:
        if __key >= self.frm and __key < self.frm + self.rng:
            return self.to + (__key - self.frm)
        else:
            return None

    def __str__(self) -> str:
        return self.__repr__()

    def __repr__(self) -> str:
        return f"{self.frm} -> {self.to} [{self.rng}]"


def unmap(lis: list[MagicDic], value: int):
    for i in lis:
        ans = i[value]
        if ans:
            return ans
    return value


def main():
    seeds = []
    maps = {}
    with open(argv[1], "r") as fp:
        src = ""
        des = ""
        for data in fp.readlines():
            if not seeds:
                seeds = list(map(int, data.split(" ")[1:]))
                seeds = [[seeds[i], seeds[i + 1]] for i in range(0, len(seeds), 2)]
                continue
            if len(data) < 2:
                continue
            if "-" in data:
                src, des = data.split("-")[0], data.split("-")[-1].split(" ")[0]
                maps[src] = [des, []]
            else:
                d_des, d_src, d_rng = list(map(int, data.split(" ")))
                maps[src][1].append(MagicDic(d_src, d_des, d_rng))
    lowest = float("INF")
    for seed in seeds:
        for k in range(seed[0], seed[0] + seed[1]):
            soil = unmap(maps["seed"][1], k)
            ferti = unmap(maps["soil"][1], soil)
            water = unmap(maps["fertilizer"][1], ferti)
            light = unmap(maps["water"][1], water)
            tmptr = unmap(maps["light"][1], light)
            hmdty = unmap(maps["temperature"][1], tmptr)
            loctn = unmap(maps["humidity"][1], hmdty)
            # print(
            #     f"Seed {seed}, soil {soil}, fertilizer {ferti}, water {water},light {light}, temperature {tmptr}, humidity {hmdty}, location {loctn}."
            # )
            if loctn < lowest:
                lowest = loctn
    print(lowest)


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
