package main

import (
	"bufio"
	"fmt"
	"os"
)

type Position struct {
	y int
	x int
}

var DIRS = []Position{
	{1, 0},
	{-1, 0},
	{0, 1},
	{0, -1},
}

func countRating(grid [][]int, start Position) int {
	result := 0

	var stack = []Position{start}
	for len(stack) > 0 {
		curr := stack[len(stack)-1]
		stack = stack[:len(stack)-1]

		if grid[curr.y][curr.x] == 9 {
			result += 1
			continue
		}

		// attempt to find next neighbour in sequence
		for _, d := range DIRS {
			y, x := curr.y+d.y, curr.x+d.x
			isOutOfRange := y < 0 || x < 0 || y == len(grid) || x == len(grid[0])
			if !isOutOfRange && grid[curr.y][curr.x]+1 == grid[y][x] {
				stack = append(stack, Position{y, x})
			}
		}
	}

	return result
}

func getTrailheadScores(grid [][]int) int {
	count := 0

	// perform dfs starting from all '0's and count how many '0-9's are in the grid
	// ratings is the same dfs algorithm as part 1, except we do not keep track of the visited cells
	// which allows us to traverse paths that we have already visited
	for i, row := range grid {
		for j, height := range row {
			if height == 0 {
				count += countRating(grid, Position{i, j})
			}
		}
	}

	return count
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var grid [][]int
	for scanner.Scan() {
		var row []int
		for _, h := range scanner.Text() {
			row = append(row, int(h)-int('0'))
		}
		grid = append(grid, row)
	}
	result := getTrailheadScores(grid)
	fmt.Println(result)
}
