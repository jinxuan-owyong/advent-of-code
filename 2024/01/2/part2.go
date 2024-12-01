package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func findSimilarity(a []int, b map[int]int) int {
	var score int = 0

	for _, key := range a {
		count, exists := b[key]
		if exists {
			score += key * count
		}
	}

	return score
}

func getFrequency(arr []int) map[int]int {
	count := make(map[int]int)

	for _, el := range arr {
		curr, ok := count[el]
		if ok {
			count[el] = curr + 1
		} else {
			count[el] = 1
		}
	}

	return count
}

func main() {
	var a []int
	var b []int

	scanner := bufio.NewScanner(os.Stdin)

	for scanner.Scan() {
		line := scanner.Text()
		values := strings.Split(line, "   ")
		if len(values) != 2 {
			panic("Malformed input")
		}
		num1, err1 := strconv.Atoi(values[0])
		num2, err2 := strconv.Atoi(values[1])
		if err1 != nil || err2 != nil {
			fmt.Println(err1, err2)
			panic("Error parsing input")
		}
		a = append(a, num1)
		b = append(b, num2)
	}

	countRight := getFrequency(b)

	result := findSimilarity(a, countRight)
	fmt.Println(result)
}
