package main

import (
	"2024/utils"
	"bufio"
	"fmt"
	"os"
	"slices"

	"github.com/emirpasic/gods/sets/hashset"
)

func isCorrectOrder(adjList map[int]*hashset.Set, update *[]int) bool {
	prev := (*update)[0]

	for i := 1; i < len(*update); i += 1 {
		curr := (*update)[i]
		forward, ok1 := adjList[prev] // skip if there is no prev, or if there is no prev -> curr
		reverse, ok2 := adjList[curr] // 29 | 13, but update contains 13 -> 29

		if ok1 && !forward.Contains(curr) || ok2 && reverse.Contains(prev) {
			return false
		}

		prev = curr
	}

	return true
}

func dfs(result *[]int, visited map[int]bool, adjList map[int]*hashset.Set, node int) {
	visited[node] = true
	neighbours, ok := adjList[node]
	if ok {
		for _, _nei := range neighbours.Values() {
			nei := _nei.(int)
			if !visited[nei] {
				dfs(result, visited, adjList, nei)
				*result = append(*result, nei)
			}
		}
	}
}

func reorderUpdate(adjList map[int]*hashset.Set, update []int) []int {
	// find the topological order of the update
	var result []int
	visited := make(map[int]bool)
	for _, k := range update {
		dfs(&result, visited, adjList, k)
		if !slices.Contains(result, k) {
			result = append(result, k)
		}
	}
	slices.Reverse(result)
	return result
}

func createGraph(rules [][]int, update []int) map[int]*hashset.Set {
	adjList := make(map[int]*hashset.Set)

	for _, rule := range rules {
		// only add edge to graph if relevant to update
		if slices.Contains(update, rule[0]) && slices.Contains(update, rule[1]) {
			edges, ok := adjList[rule[0]]
			if ok {
				edges.Add(rule[1])
			} else {
				s := hashset.New(rule[1])
				adjList[rule[0]] = s
			}
		}
	}

	return adjList
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var updates [][]int
	var rules [][]int

	for {
		scanner.Scan()
		line := scanner.Text()
		if len(line) == 0 {
			break
		}
		rules = append(rules, utils.ParseArrInt(line, "|"))
	}

	for scanner.Scan() {
		line := scanner.Text()
		updates = append(updates, utils.ParseArrInt(line, ","))

	}

	result := 0
	for _, update := range updates {
		adjList := createGraph(rules, update)

		if !isCorrectOrder(adjList, &update) {
			topo := reorderUpdate(adjList, update)
			result += topo[len(topo)/2]
		}
	}

	fmt.Println(result)
}
