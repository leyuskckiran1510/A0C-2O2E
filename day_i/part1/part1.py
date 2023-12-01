print(
    sum(
        [
            (
                lambda x: int(
                    f"{list(filter(lambda x: x>='0' and x<='9',x))[0]}{list(filter(lambda x: x>='0' and x<='9',x))[-1]}"
                )
            )(i)
            for i in open("input.txt", "r").readlines()
        ]
    )
)
