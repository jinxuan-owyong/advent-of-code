# 2024

## Running

```sh
go run partX.go < puzzle.in
```

## Debugging

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

| Day | Title                 | Part 1             | Part 2              |
| --- | --------------------- | ------------------ | ------------------- |
| 1   | Historian Hysteria    | Array, Sorting     | HashMap             |
| 2   | Red-Nosed Reports     | Array              | Brute Force         |
| 3   | Mull It Over          | Regexp             | Regexp              |
| 4   | Ceres Search          | DFS                | Brute Force         |
| 5   | Print Queue           | Graph              | Topological Sorting |
| 6   | Guard Gallivant       | Array, Simulation  | Brute Force*        |
| 7   | Bridge Repair         | Recursion          | Backtracking        |
| 8   | Resonant Collinearity | Array, HashSet     | Array, HashSet      |
| 9   | Disk Fragmenter       | Two Pointers       | Binary Heap         |
| 10  | Hoof It               | Depth-First Search | Depth-First Search  |
