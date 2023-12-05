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


def main():
    seeds = []
    maps = {}
    with open(argv[1], "r") as fp:
        des = ""
        for data in fp.readlines():
            if not seeds:
                seeds = list(map(int, data.split(" ")[1:]))
                seeds = [[seeds[i], seeds[i + 1]] for i in range(0, len(seeds), 2)]
                continue
            if len(data) < 2:
                continue
            if "-" in data:
                des = data.split("-")[-1].split(" ")[0]
            else:
                new = list(map(int, data.split(" ")))
                maps[des] = maps.get(des, []) + [new]

    print(seeds, maps)


if __name__ == "__main__":
    if len(argv) < 2:
        print("Provide A input File")
    else:
        main()
