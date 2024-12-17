package main

import (
	"2024/utils"
	"bufio"
	"fmt"
	"os"

	"github.com/emirpasic/gods/sets/hashset"
)

func isCorrectOrder(adjList *map[int]*hashset.Set, update *[]int) bool {
	prev := (*update)[0]

	for i := 1; i < len(*update); i += 1 {
		curr := (*update)[i]
		forward, ok1 := (*adjList)[prev] // skip if there is no prev, or if there is no prev -> curr
		reverse, ok2 := (*adjList)[curr] // 29 | 13, but update contains 13 -> 29

		if ok1 && !forward.Contains(curr) || ok2 && reverse.Contains(prev) {
			return false
		}

		prev = curr
	}

	return true
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	adjList := make(map[int]*hashset.Set)
	var updates [][]int

	for {
		scanner.Scan()
		line := scanner.Text()
		if len(line) == 0 {
			break
		}

		rule := utils.ParseArrInt(line, "|")
		edges, ok := adjList[rule[0]]
		if ok {
			edges.Add(rule[1])
		} else {
			s := hashset.New(rule[1])
			adjList[rule[0]] = s
		}
	}

	for scanner.Scan() {
		line := scanner.Text()
		updates = append(updates, utils.ParseArrInt(line, ","))

	}

	result := 0
	for _, update := range updates {
		if isCorrectOrder(&adjList, &update) {
			result += update[len(update)/2]
		}
	}

	fmt.Println(result)
}
