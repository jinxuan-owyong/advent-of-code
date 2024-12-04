package main

import (
	"bufio"
	"fmt"
	"os"
)

func checkX(puzzle *[]string, i int, j int, abcd string) int {
	/*
		puzzle[i][j] = Z
		A B
		 Z
		C D
	*/
	if i < 1 || j < 1 || i >= len(*puzzle)-1 || j >= len((*puzzle)[i])-1 {
		return 0
	}
	if (*puzzle)[i-1][j-1] == abcd[0] && (*puzzle)[i-1][j+1] == abcd[1] && (*puzzle)[i+1][j-1] == abcd[2] && (*puzzle)[i+1][j+1] == abcd[3] {
		return 1
	}
	return 0
}

func countXmas(puzzle *[]string) int {
	result := 0

	for i := 1; i < len(*puzzle)-1; i += 1 {
		for j := 1; j < len((*puzzle)[i])-1; j += 1 {
			count := 0
			if (*puzzle)[i][j] == 'A' {
				count += checkX(puzzle, i, j, "MMSS")
				count += checkX(puzzle, i, j, "SSMM")
				count += checkX(puzzle, i, j, "SMSM")
				count += checkX(puzzle, i, j, "MSMS")
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
