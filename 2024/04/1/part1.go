package main

import (
	"bufio"
	"fmt"
	"os"
)

const target string = "XMAS"

func dfs(puzzle *[]string, i int, j int, dy int, dx int, pos int) int {
	if pos == len(target) {
		return 1
	}

	if i < 0 || j < 0 || i == len(*puzzle) || j == len((*puzzle)[i]) || (*puzzle)[i][j] != target[pos] {
		return 0
	}

	return dfs(puzzle, i+dy, j+dx, dy, dx, pos+1)
}

func countXmas(puzzle *[]string) int {
	result := 0

	for i := 0; i < len(*puzzle); i += 1 {
		for j := 0; j < len((*puzzle)[i]); j += 1 {
			count := 0
			if (*puzzle)[i][j] == 'X' {
				count += dfs(puzzle, i, j, -1, 0, 0)
				count += dfs(puzzle, i, j, 1, 0, 0)
				count += dfs(puzzle, i, j, 0, -1, 0)
				count += dfs(puzzle, i, j, 0, 1, 0)
				count += dfs(puzzle, i, j, -1, -1, 0)
				count += dfs(puzzle, i, j, -1, 1, 0)
				count += dfs(puzzle, i, j, 1, -1, 0)
				count += dfs(puzzle, i, j, 1, 1, 0)
			}
			result += count
		}
	}

	return result
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var puzzle []string
	for scanner.Scan() {
		puzzle = append(puzzle, scanner.Text())
	}
	result := countXmas(&puzzle)
	fmt.Println(result)
}
