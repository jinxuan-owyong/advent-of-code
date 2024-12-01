package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

func compareLists(a []int, b []int) int {
	var result int = 0

	sort.Slice(a, func(i int, j int) bool {
		return a[i] < a[j]
	})
	sort.Slice(b, func(i int, j int) bool {
		return b[i] < b[j]
	})

	for i := range len(a) {
		var diff int = a[i] - b[i]
		if diff < 0 {
			diff *= -1
		}
		result += diff
	}

	return result
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

	result := compareLists(a, b)
	fmt.Println(result)
}
