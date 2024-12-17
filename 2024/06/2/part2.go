package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Direction struct {
	dy int
	dx int
}

func findStart(grid [][]rune) (int, int) {
	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] == '^' {
				return i, j
			}
		}
	}
	panic(false)
}

func getKey(y, x, curr int) string {
	var b strings.Builder
	b.WriteString(strconv.Itoa(y))
	b.WriteRune(',')
	b.WriteString(strconv.Itoa(x))
	b.WriteRune(',')
	b.WriteString(strconv.Itoa(curr))
	return b.String()
}

func hasLoop(grid [][]rune, y int, x int) (bool, int, int) {
	var DIRS = []Direction{
		{-1, 0}, // up
		{0, 1},  // right
		{1, 0},  // down
		{0, -1}, // left
	}

	// goal: distinct positions the guard will visit before leaving the mapped area
	curr := 0
	visited := make(map[string]bool) // y, x, dir

	for {
		key := getKey(y, x, curr)
		if _, exists := visited[key]; exists {
			return true, y, x
		}

		dy := DIRS[curr].dy
		dx := DIRS[curr].dx

		// move in direction until obstacle/boundary reached
		for y+dy >= 0 && y+dy < len(grid) && x+dx >= 0 && x+dx < len(grid[0]) && grid[y+dy][x+dx] != '#' {
			y, x = y+dy, x+dx
			visited[getKey(y, x, curr)] = true
		}

		// guard leaves the mapped area
		if !(y+dy >= 0 && y+dy < len(grid) && x+dx >= 0 && x+dx < len(grid[0])) {
			break
		}

		visited[key] = true
		curr = (curr + 1) % len(DIRS) // turn right 90 degrees
	}

	return false, -1, -1
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var grid [][]rune
	for scanner.Scan() {
		s := scanner.Text()
		row := []rune{}
		for _, r := range s {
			row = append(row, r)
		}
		grid = append(grid, row)
	}

	result := 0
	y, x := findStart(grid)
	positions := make([][]rune, len(grid))
	copy(positions, grid)

	for i := range grid {
		for j := range grid[i] {
			if grid[i][j] == '#' || grid[i][j] == '^' {
				continue
			}
			grid[i][j] = '#'
			// enhancement: instead of blindly inserting obstacles, only insert at guarded cells
			if exists, i, j := hasLoop(grid, y, x); exists {
				positions[i][j] = 'O'
				result += 1
			}
			grid[i][j] = '.'
		}
	}

	for _, row := range positions {
		fmt.Println(string(row))
	}
	fmt.Println(result)
}
