package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"

	"github.com/emirpasic/gods/sets/hashset"
	"github.com/samber/lo"
)

type Position struct {
	y int
	x int
}

func (p Position) GetKey() string {
	var s strings.Builder
	s.WriteString(strconv.Itoa(p.y))
	s.WriteRune('#')
	s.WriteString(strconv.Itoa(p.x))
	return s.String()
}

func (p Position) isWithinRange(grid [][]rune) bool {
	return p.y >= 0 && p.y < len(grid) && p.x >= 0 && p.x < len(grid[0])
}

func findAntiNodes(grid [][]rune, antennas []Position, antinodes *hashset.Set) {
	for i, a := range antennas {
		for _, b := range antennas[i+1:] {
			// search in straight line in both directions from antennas
			dy := b.y - a.y
			dx := b.x - a.x
			offset := 0 // include the other antenna as well
			isValid := true
			for isValid {
				isValid = false

				if p1 := (Position{a.y - dy*offset, a.x - dx*offset}); p1.isWithinRange(grid) {
					antinodes.Add(p1.GetKey())
					isValid = true
					if grid[p1.y][p1.x] == '.' {
						grid[p1.y][p1.x] = '#'
					}
				}

				if p2 := (Position{b.y + dy*offset, b.x + dx*offset}); p2.isWithinRange(grid) {
					antinodes.Add(p2.GetKey())
					isValid = true
					if grid[p2.y][p2.x] == '.' {
						grid[p2.y][p2.x] = '#'
					}
				}

				offset += 1
			}
		}
	}
}

func analyzeSignals(grid [][]rune) int {
	// identify positions of matching antennas
	antennas := make(map[rune][]Position, 62)
	for i, row := range grid {
		for j, a := range row {
			if a != '.' {
				antennas[a] = append(antennas[a], Position{i, j})
			}
		}
	}

	antennaRunes := [][]rune{
		{'a', 'z'},
		{'A', 'Z'},
		{'0', '9'},
	}

	// it is possible that 3 same-type antennas create non-unique antinodes locations
	// we also account for overlap across antenna types
	antinodes := hashset.New()

	for _, runes := range antennaRunes {
		for c := runes[0]; c <= runes[1]; c += 1 {
			findAntiNodes(grid, antennas[c], antinodes)
		}
	}

	return antinodes.Size()
}

func readableGrid(grid [][]rune) []string {
	return lo.Map(grid, func(row []rune, _ int) string {
		return string(row)
	})
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
	result := analyzeSignals(grid)
	for _, row := range readableGrid(grid) {
		fmt.Println(row)
	}
	fmt.Println(result) // > 229
}
