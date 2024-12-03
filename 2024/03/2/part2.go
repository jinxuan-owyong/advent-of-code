package main

import (
	"2024/utils"
	"bufio"
	"fmt"
	"os"
	"regexp"
)

func scanMemory(mem string, do bool) (int, bool) {
	result := 0

	re := regexp.MustCompile(`(do\(\))|(mul\((\d{1,3}),(\d{1,3})\))|(don't\(\))`)
	instructions := re.FindAllStringSubmatch(mem, -1)
	i := 0

	for i < len(instructions) {
		if instructions[i][0] == "don't()" {
			do = false
		} else if instructions[i][0] == "do()" {
			do = true
		} else if do {
			// disabled until dont is false
			x := utils.ParseInt(instructions[i][3])
			y := utils.ParseInt(instructions[i][4])
			result += x * y
		}
		i += 1
	}

	return result, do
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	result := 0
	do := true
	for scanner.Scan() {
		// do state should be carried over multiple lines
		sum, next := scanMemory(scanner.Text(), do)
		result += sum
		do = next
	}
	fmt.Println(result)
}
