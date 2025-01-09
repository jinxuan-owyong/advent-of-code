package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func removeLeadingZeroes(s string) string {
	// increment i until it is pointing at the last character, or there are no more leading zeroes
	i := 0
	for i < len(s)-1 && s[i] == '0' {
		i += 1
	}
	return s[i:]
}

func blink(stones []string) []string {
	var result []string
	for _, curr := range stones {
		if curr == "0" {
			result = append(result, "1")
		} else if len(curr)%2 == 0 {
			mid := len(curr) / 2
			left, right := curr[:mid], removeLeadingZeroes(curr[mid:])
			result = append(result, left, right)
		} else {
			s, _ := strconv.Atoi(curr)
			result = append(result, strconv.Itoa(s*2024))
		}
	}
	return result
}

func evaluate(stones []string, blinks int) int {
	for range blinks {
		stones = blink(stones)
	}

	return len(stones)
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Scan()
	var stones = strings.Split(scanner.Text(), " ")
	scanner.Scan()
	var blinks, _ = strconv.Atoi(scanner.Text())
	result := evaluate(stones, blinks)
	fmt.Println(result)
}
