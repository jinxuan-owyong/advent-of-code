# advent-of-code

- [2022 (Python)](https://github.com/jinxuan-owyong/advent-of-code/tree/main/2022)
- [2023 (Python)](https://github.com/jinxuan-owyong/advent-of-code/tree/main/2023)
- [2024 (Go)](https://github.com/jinxuan-owyong/advent-of-code/tree/main/2024)
- [2025 (Go)](https://github.com/jinxuan-owyong/advent-of-code/tree/main/2025)

## Retrieving puzzles

`day` and `year` default to "today" as per `US/Eastern` in line with Advent of Code's release

```sh
bash getPuzzle.sh [<day>] [<year>]
```

## Go

### Running

```sh
go run partX.go < puzzle.in
```

### Debugging

Use the following `launch.json` to start the debugger. Enter inputs as required in the integrated terminal, and at the end of the input, use ^D to indicate EOF

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Launch Package",
            "type": "go",
            "request": "launch",
            "mode": "auto",
            "program": "${fileDirname}",
            "console": "integratedTerminal"
        }
    ]
}
```