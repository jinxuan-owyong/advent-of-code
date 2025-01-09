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

func key(stone string, N int) string {
	var s strings.Builder
	s.WriteString(stone)
	s.WriteRune('#')
	s.WriteString(strconv.Itoa(N))
	return s.String()
}

func blink(stone string, N int, cache map[string]int) int {
	if N == 0 {
		return 1
	}

	if val, exists := cache[key(stone, N)]; exists {
		return val
	}

	var count int = 0
	if stone == "0" {
		count += blink("1", N-1, cache)
	} else if len(stone)%2 == 0 {
		mid := len(stone) / 2
		left, right := stone[:mid], removeLeadingZeroes(stone[mid:])
		count += blink(left, N-1, cache)
		count += blink(right, N-1, cache)
	} else {
		s, _ := strconv.Atoi(stone)
		count += blink(strconv.Itoa(s*2024), N-1, cache)
	}

	cache[key(stone, N)] = count
	return count
}

func evaluate(stones []string, N int) int {
	cache := make(map[string]int)

	// the order of the numbers do not matter, since we are after the number of stones in the end
	var total int = 0
	for _, stone := range stones {
		total += blink(stone, N, cache)
	}

	return total
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
