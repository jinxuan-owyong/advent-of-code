package main

import (
	"2024/utils"
	"bufio"
	"fmt"
	"os"
	"regexp"
)

func scanMemory(mem string) int {
	result := 0

	re := regexp.MustCompile(`mul\((\d{1,3}),(\d{1,3})\)`)
	instructions := re.FindAllStringSubmatch(mem, -1)
	for _, instruction := range instructions {
		x := utils.ParseInt(instruction[1])
		y := utils.ParseInt(instruction[2])
		result += x * y
	}

	return result
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	result := 0
	for scanner.Scan() {
		result += scanMemory(scanner.Text())
	}
	fmt.Println(result)
}
