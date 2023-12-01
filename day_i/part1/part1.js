const input = ``

console.log(input.split("\n")
    .map(x => 
        parseInt(
            (
                Array(...x)
                    .filter(x => x >= '0' && x <= '9')[0]
            ) + 
            Array(...x)
                .filter(x => x >= '0' && x <= '9').reduce((x, y) => y))
    ).reduce((x, y) => x + y)
)